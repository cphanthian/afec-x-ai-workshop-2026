# AFEC-X AI Workshop 2026

Hands-on introduction to **supervised** and **unsupervised learning** for biodiversity monitoring.

This repository is intentionally lightweight. Students only need Python, VS Code, and a few common packages. No GPU, CUDA, PyTorch, or TensorFlow installation is required.

## Workshop flow

### Part 1 — Supervised learning: Teachable Machine

Students train an image classifier using four butterfly species:

- *Danaus chrysippus*
- *Danaus genutia*
- *Acraea terpsicore*
- *Papilio polytes*

After testing on held-out images of the same species, the model is challenged with an unseen fifth species:

- *Eurema hecabe*

**Question:** What does a closed-set classifier do when the correct biological class was never included in training?

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
├── setup_windows.ps1
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

The final image dataset should be downloaded and visually audited before class. Keep the unknown butterfly species out of Teachable Machine training. Keep the flower answer key hidden until the final reveal.

## Take-home message

> AI outputs are evidence to evaluate, not biological truth to accept.
