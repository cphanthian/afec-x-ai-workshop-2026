from pathlib import Path
from io import BytesIO
import csv
import random
import shutil
import time

import requests
from PIL import Image


SEED = 42
BASE_DIR = Path("afec_workshop_dataset")
API_URL = "https://api.inaturalist.org/v1/observations"
PER_PAGE = 200
MAX_PAGES = 10
REQUEST_DELAY = 1.05
DOWNLOAD_RETRIES = 3
CLEAN_OLD_DATASET = True

BUTTERFLIES = {
    "Danaus_chrysippus": {"taxon_name": "Danaus chrysippus", "train": 12, "test": 4},
    "Danaus_genutia": {"taxon_name": "Danaus genutia", "train": 12, "test": 4},
    "Acraea_terpsicore": {"taxon_name": "Acraea terpsicore", "train": 12, "test": 4},
    "Papilio_polytes": {"taxon_name": "Papilio polytes", "train": 12, "test": 4},
}

UNKNOWN = {
    "Eurema_hecabe": {"taxon_name": "Eurema hecabe", "test": 8},
}

CAMPANULA = [
    "Campanula rotundifolia",
    "Campanula persicifolia",
    "Campanula glomerata",
    "Campanula rapunculoides",
    "Campanula medium",
    "Campanula carpatica",
]

FLOWER_PER_SPECIES = 8

session = requests.Session()
session.headers.update({"User-Agent": "AFEC-X-AI-Workshop-2026"})


def get_observations(taxon_name):
    observations = []
    print(f"\nSearching iNaturalist: {taxon_name}")

    for page in range(1, MAX_PAGES + 1):
        params = {
            "taxon_name": taxon_name,
            "quality_grade": "research",
            "has[]": "photos",
            "per_page": PER_PAGE,
            "page": page,
            "order_by": "id",
            "order": "desc",
        }

        response = session.get(API_URL, params=params, timeout=60)
        response.raise_for_status()
        results = response.json().get("results", [])

        if not results:
            break

        observations.extend(results)
        print(f"  page {page}: {len(results)} observations | pool={len(observations)}")

        if len(results) < PER_PAGE:
            break

        time.sleep(REQUEST_DELAY)

    return observations


def extract_photo_records(observations):
    records = []
    seen_photo_ids = set()

    for observation in observations:
        photos = observation.get("photos") or []
        if not photos:
            continue

        taxon = observation.get("taxon") or {}
        user = observation.get("user") or {}

        for photo in photos:
            photo_id = photo.get("id")
            url = photo.get("url")

            if photo_id is None or not url or photo_id in seen_photo_ids:
                continue

            image_url = (
                url.replace("square.", "medium.")
                   .replace("small.", "medium.")
                   .replace("thumb.", "medium.")
            )

            records.append({
                "observation_id": observation.get("id"),
                "photo_id": photo_id,
                "scientific_name": taxon.get("name", ""),
                "taxon_rank": taxon.get("rank", ""),
                "observer": user.get("login", ""),
                "license": photo.get("license_code") or "",
                "attribution": photo.get("attribution") or "",
                "image_url": image_url,
                "observation_url": (
                    "https://www.inaturalist.org/observations/"
                    f"{observation.get('id')}"
                ),
            })

            seen_photo_ids.add(photo_id)
            break

    return records


def get_candidate_pool(taxon_name):
    records = extract_photo_records(get_observations(taxon_name))

    unique = {record["photo_id"]: record for record in records}
    records = list(unique.values())

    rng = random.Random(f"{SEED}-{taxon_name}")
    rng.shuffle(records)

    print(f"  candidate photos: {len(records)}")

    if not records:
        raise RuntimeError(f"No usable photos found for {taxon_name}")

    return records


def download_and_validate(url, output_path):
    for attempt in range(1, DOWNLOAD_RETRIES + 1):
        try:
            response = session.get(url, timeout=60)
            response.raise_for_status()

            content = response.content

            test_image = Image.open(BytesIO(content))
            test_image.verify()

            image = Image.open(BytesIO(content)).convert("RGB")
            width, height = image.size

            if width < 200 or height < 200:
                raise ValueError(f"Image too small: {width} x {height}")

            output_path.parent.mkdir(parents=True, exist_ok=True)
            image.save(output_path, format="JPEG", quality=92, optimize=True)
            return True

        except Exception as error:
            print(f"    attempt {attempt}/{DOWNLOAD_RETRIES} failed: {error}")
            if attempt < DOWNLOAD_RETRIES:
                time.sleep(2)

    return False


def make_metadata_row(record, section, taxon_name, filename, output_path):
    row = record.copy()
    row.update({
        "dataset_section": section,
        "requested_taxon": taxon_name,
        "filename": filename,
        "relative_path": str(output_path.relative_to(BASE_DIR)),
    })
    return row


def collect_images(taxon_name, n_required, output_dir, filename_prefix, section):
    candidates = get_candidate_pool(taxon_name)

    if len(candidates) < n_required:
        raise RuntimeError(
            f"Not enough photographs for {taxon_name}: "
            f"need {n_required}, found {len(candidates)}"
        )

    downloaded = []

    for record in candidates:
        if len(downloaded) >= n_required:
            break

        number = len(downloaded) + 1
        filename = f"{filename_prefix}_{number:02d}.jpg"
        output_path = output_dir / filename

        print(f"  downloading {number}/{n_required}: {filename}")

        if not download_and_validate(record["image_url"], output_path):
            continue

        downloaded.append(
            make_metadata_row(
                record, section, taxon_name, filename, output_path
            )
        )
        time.sleep(0.25)

    if len(downloaded) < n_required:
        raise RuntimeError(
            f"Only {len(downloaded)}/{n_required} valid images "
            f"could be downloaded for {taxon_name}"
        )

    return downloaded


if CLEAN_OLD_DATASET and BASE_DIR.exists():
    print(f"Removing old dataset: {BASE_DIR.resolve()}")
    shutil.rmtree(BASE_DIR)

metadata = []

# Known butterflies: shared candidate pool prevents train/test overlap.
for folder_name, config in BUTTERFLIES.items():
    taxon_name = config["taxon_name"]
    candidates = get_candidate_pool(taxon_name)
    candidate_index = 0

    for section_name, n_required, output_dir, filename_kind in [
        (
            "supervised_train",
            config["train"],
            BASE_DIR / "data" / "supervised" / "train" / folder_name,
            "train",
        ),
        (
            "supervised_test_known",
            config["test"],
            BASE_DIR / "data" / "supervised" / "test" / "known" / folder_name,
            "test",
        ),
    ]:
        count = 0

        while count < n_required:
            if candidate_index >= len(candidates):
                raise RuntimeError(f"Candidate pool exhausted for {taxon_name}")

            record = candidates[candidate_index]
            candidate_index += 1

            filename = f"{folder_name}_{filename_kind}_{count + 1:02d}.jpg"
            output_path = output_dir / filename

            print(f"  {filename_kind.upper()} {count + 1}/{n_required}: {filename}")

            if not download_and_validate(record["image_url"], output_path):
                continue

            metadata.append(
                make_metadata_row(
                    record, section_name, taxon_name, filename, output_path
                )
            )
            count += 1
            time.sleep(0.25)

# Unknown butterfly
for folder_name, config in UNKNOWN.items():
    metadata.extend(
        collect_images(
            config["taxon_name"],
            config["test"],
            BASE_DIR / "data" / "supervised" / "test" / "unknown" / folder_name,
            folder_name,
            "supervised_test_unknown",
        )
    )

# Flowers: download into temporary species folders first.
flower_metadata = []
temp_flower_dir = BASE_DIR / "_temporary_flowers"

for species_number, species in enumerate(CAMPANULA, start=1):
    flower_metadata.extend(
        collect_images(
            species,
            FLOWER_PER_SPECIES,
            temp_flower_dir / f"species_{species_number:02d}",
            f"species_{species_number:02d}",
            "unsupervised_flowers",
        )
    )

# Hide flower species names from students.
rng = random.Random(SEED)
rng.shuffle(flower_metadata)

final_flower_dir = BASE_DIR / "data" / "unsupervised" / "flowers"
final_flower_dir.mkdir(parents=True, exist_ok=True)

for number, row in enumerate(flower_metadata, start=1):
    old_path = BASE_DIR / row["relative_path"]
    new_filename = f"flower_{number:03d}.jpg"
    new_path = final_flower_dir / new_filename
    old_path.replace(new_path)

    row["filename"] = new_filename
    row["relative_path"] = str(new_path.relative_to(BASE_DIR))

metadata.extend(flower_metadata)

if temp_flower_dir.exists():
    shutil.rmtree(temp_flower_dir)

# Full metadata
metadata_file = BASE_DIR / "data" / "image_metadata.csv"
metadata_file.parent.mkdir(parents=True, exist_ok=True)

fields = [
    "dataset_section",
    "requested_taxon",
    "scientific_name",
    "taxon_rank",
    "filename",
    "relative_path",
    "observation_id",
    "photo_id",
    "observer",
    "license",
    "attribution",
    "image_url",
    "observation_url",
]

with metadata_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for row in metadata:
        writer.writerow({field: row.get(field, "") for field in fields})

# Instructor-only flower answer key.
answer_key = BASE_DIR / "data" / "unsupervised" / "flower_answer_key.csv"

with answer_key.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["filename", "species", "observation_id"])
    writer.writeheader()

    for row in flower_metadata:
        writer.writerow({
            "filename": row["filename"],
            "species": row["requested_taxon"],
            "observation_id": row["observation_id"],
        })

print("\n" + "=" * 60)
print("AFEC-X WORKSHOP DATASET COMPLETE")
print("=" * 60)
print(f"Dataset root: {BASE_DIR.resolve()}")
print(f"Total images: {len(metadata)}")
print(f"Metadata: {metadata_file.resolve()}")
print(f"Flower answer key: {answer_key.resolve()}")
print("\nExpected total: 120 images")
print("Keep Eurema hecabe out of Teachable Machine training.")
print("Keep flower_answer_key.csv hidden until the final reveal.")
