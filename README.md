# AFEC-X AI Workshop 2026

Hands-on introduction to **supervised** and **unsupervised learning** for biodiversity monitoring.

This repository is intentionally lightweight. Students only need Python, VS Code, and a few common packages. No GPU, CUDA, PyTorch, or TensorFlow installation is required.

## Workshop flow

### Part 1 — Supervised learning: browser-based image classifier

Students can use **any one** of these browser tools:

1. **Teachable Machine — Image Project**  
   https://teachablemachine.withgoogle.com/train/image

2. **SkillSafe Image Trainer**  
   https://image-trainer.skillsafe.ai/

3. **WebAI Playground — Image Classifier**  
   https://mlhs.ink/Playground/

Use whichever service is accessible on the workshop network. The biological exercise and dataset are the same for all three tools.

Students train an image classifier using four butterfly species:

- *Danaus chrysippus*
- *Danaus genutia*
- *Acraea terpsicore*
- *Papilio polytes*

After testing on held-out images of the same species, the model is challenged with an unseen fifth species:

- *Eurema hecabe*

**Question:** What does a closed-set classifier do when the correct biological class was never included in training?

Detailed instructions are provided in `notebooks/SUPERVISED_HANDS_ON.md`.

### Part 2 — Unsupervised learning: flower clustering

Students use a Jupyter notebook to explore a set of visually similar but diverse *Campanula* flower images.

Workflow:

```text
Images
  ↓
Simple numerical colour features
  ↓
Feature standardization
  ↓
PCA visualization
  ↓
K-means clustering
  ↓
Human interpretation
```

The biological labels are hidden during the activity. Students vary K, inspect the clusters, use an elbow plot, and finally learn that the images were sampled from six biological species.

**Question:** Do clusters found in feature space automatically correspond to biological species?

## Repository structure

```text
afec-x-ai-workshop-2026/
├── README.md
├── requirements.txt
├── SUPERVISED_HANDS_ON.md
├── STUDENT_SETUP_WINDOWS.md
├── STUDENT_SETUP_MACOS.md
├── setup_windows.ps1
├── setup_macos.sh
├── scripts/
│   └── download_workshop_dataset.py
├── data/
│   ├── README.md
│   ├── supervised/
│   │   ├── train/
│   │   └── test/
│   │       ├── known/
│   │       └── unknown/
│   └── unsupervised/
│       └── flowers/
└── notebooks/
    └── 01_flower_kmeans_student.ipynb
```

## Quick setup

### Windows

From PowerShell in the repository folder:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup_windows.ps1
```

See `STUDENT_SETUP_WINDOWS.md` for the full zero-to-ready guide.

### macOS

From Terminal in the repository folder:

```bash
bash setup_macos.sh
```

See `STUDENT_SETUP_MACOS.md` for the full zero-to-ready guide.

---

## Windows setup

### 1. Install Python 3.11

In PowerShell:

```powershell
winget install -e --id Python.Python.3.11
```

Close PowerShell and open it again, then check:

```powershell
python --version
```

### 2. Clone this repository

```powershell
git clone https://github.com/cphanthian/afec-x-ai-workshop-2026.git
cd afec-x-ai-workshop-2026
```

### 3. Create a virtual environment

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4. Install packages

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Open VS Code

```powershell
code .
```

Install the **Python** and **Jupyter** extensions in VS Code if needed. Open the notebook and select the interpreter from:

```text
.venv\Scripts\python.exe
```

## Instructor note

The final image dataset should be downloaded and visually audited before class. Keep the unknown butterfly species out of the supervised classifier training set, regardless of which browser tool is used. Keep the flower answer key hidden until the final reveal.

## Take-home message

> AI outputs are evidence to evaluate, not biological truth to accept.
