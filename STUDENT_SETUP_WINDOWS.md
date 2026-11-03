# AFEC-X 2026 — Student Setup Manual

This guide is written for students who are starting from **zero** on a Windows computer.

You do **not** need prior Python experience.

By the end of this setup, you will be able to:

- download the workshop files from GitHub;
- open the project in VS Code;
- create an isolated Python environment;
- install the required packages;
- open and run a Jupyter Notebook.

---

# 1. What you need

You need:

- a Windows computer;
- an internet connection;
- about 2–3 GB of free disk space;
- permission to install software.

You do **not** need:

- Anaconda;
- Anaconda Navigator;
- CUDA;
- a GPU;
- PyTorch;
- TensorFlow.

---

# 2. Open PowerShell

Press:

```text
Windows key
```

Type:

```text
PowerShell
```

Open **Windows PowerShell** or **PowerShell**.

You should see a window similar to:

```text
PS C:\Users\YourName>
```

All commands in this manual should be entered into PowerShell unless stated otherwise.

---

# 3. Check whether Winget is available

Run:

```powershell
winget --version
```

If you see a version number, continue to the next step.

If PowerShell says that `winget` is not recognized, install or update **App Installer** from the Microsoft Store, then reopen PowerShell.

---

# 4. Install Git

Run:

```powershell
winget install -e --id Git.Git
```

After installation, close PowerShell and open it again.

Check:

```powershell
git --version
```

You should see something similar to:

```text
git version 2.x.x
```

---

# 5. Install Python 3.11

Run:

```powershell
winget install -e --id Python.Python.3.11
```

After installation, close PowerShell and open it again.

Check:

```powershell
python --version
```

Expected output:

```text
Python 3.11.x
```

If `python` is not recognized, try:

```powershell
py --version
```

If `py` works but `python` does not, tell the instructor before continuing.

---

# 6. Install Visual Studio Code

Run:

```powershell
winget install -e --id Microsoft.VisualStudioCode
```

After installation, close PowerShell and open it again.

Check:

```powershell
code --version
```

If a version number appears, VS Code is ready.

---

# 7. Install the VS Code Python and Jupyter extensions

Run:

```powershell
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
```

These extensions allow VS Code to run Python and `.ipynb` Jupyter Notebook files.

---

# 8. Go to your Desktop

Run:

```powershell
cd $HOME\Desktop
```

Check your current folder:

```powershell
pwd
```

You should see a path ending in:

```text
Desktop
```

---

# 9. Download the workshop repository

Run:

```powershell
git clone https://github.com/cphanthian/afec-x-ai-workshop-2026.git
```

Then enter the workshop folder:

```powershell
cd afec-x-ai-workshop-2026
```

Check the files:

```powershell
dir
```

You should see files and folders such as:

```text
README.md
requirements.txt
setup_windows.ps1
data
notebooks
scripts
```

---

# 10. Create a Python virtual environment

A virtual environment keeps the workshop packages separate from the rest of your computer.

Run:

```powershell
python -m venv .venv
```

This creates a hidden folder called:

```text
.venv
```

inside the workshop repository.

---

# 11. Allow PowerShell to activate the environment

Windows may block local PowerShell scripts by default.

For this PowerShell session only, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

This setting disappears when you close the PowerShell window.

---

# 12. Activate the environment

Run:

```powershell
.\.venv\Scripts\Activate.ps1
```

If successful, the beginning of the PowerShell prompt should change to something similar to:

```text
(.venv) PS C:\Users\YourName\Desktop\afec-x-ai-workshop-2026>
```

The important part is:

```text
(.venv)
```

---

# 13. Install the workshop Python packages

First update pip:

```powershell
python -m pip install --upgrade pip
```

Then install the workshop requirements:

```powershell
python -m pip install -r requirements.txt
```

This installs the packages used in the workshop, including:

- NumPy;
- Matplotlib;
- Pillow;
- scikit-learn;
- Jupyter;
- ipykernel;
- requests.

No GPU libraries are required.

---

# 14. Check that Python is using the workshop environment

Run:

```powershell
python -c "import sys; print(sys.executable)"
```

The output should contain:

```text
afec-x-ai-workshop-2026\.venv\Scripts\python.exe
```

Then test the main packages:

```powershell
python -c "import numpy, matplotlib, PIL, sklearn; print('Workshop environment OK')"
```

Expected output:

```text
Workshop environment OK
```

---

# 15. Open the workshop in VS Code

While still inside the workshop folder, run:

```powershell
code .
```

VS Code should open the entire repository.

---

# 16. Open the Jupyter Notebook

In the VS Code Explorer on the left side, open:

```text
notebooks
└── 01_flower_kmeans_student.ipynb
```

Click:

```text
01_flower_kmeans_student.ipynb
```

The notebook should open in VS Code.

---

# 17. Select the correct Python kernel

At the top-right of the notebook, click:

```text
Select Kernel
```

Choose:

```text
Python Environments
```

Then select the Python environment whose path contains:

```text
.venv\Scripts\python.exe
```

Do **not** select another Python installation if `.venv` is available.

---

# 18. Test the notebook

Run the first Python code cell.

You can click the small:

```text
▶
```

button next to the code cell.

If the imports run without an error, your environment is ready.

---

# 19. Workshop dataset

The final workshop repository will contain the datasets under:

```text
data/
├── supervised/
└── unsupervised/
```

For the supervised activity, the butterfly images will be used with **Teachable Machine**.

For the unsupervised activity, the notebook will read flower images from:

```text
data/unsupervised/flowers/
```

You do not need to manually move these images if you cloned the final workshop repository.

---

# 20. Supervised-learning activity

For this part of the workshop, no Python code is required.

We will use Teachable Machine in a web browser.

The training dataset contains four butterfly species.

A fifth species is kept separate and will be used later as an unknown-species challenge.

Follow the instructor during the workshop and do not mix the unknown-species images into the training data.

---

# 21. Unsupervised-learning activity

Open:

```text
notebooks/01_flower_kmeans_student.ipynb
```

We will work through the notebook step by step.

The workflow is:

```text
Flower images
      ↓
Numerical colour features
      ↓
Feature standardization
      ↓
PCA visualization
      ↓
K-means clustering
      ↓
Interpretation
```

You do not need to understand all of the code before the activity begins.

---

# 22. The next time you open the workshop

You do **not** need to reinstall Python or the packages.

Open PowerShell and run:

```powershell
cd $HOME\Desktop\afec-x-ai-workshop-2026

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\.venv\Scripts\Activate.ps1

code .
```

Then open the notebook and select the `.venv` kernel.

---

# 23. Updating the workshop files

If the instructor tells you that the repository has been updated, close the notebook and run:

```powershell
cd $HOME\Desktop\afec-x-ai-workshop-2026
git pull
```

Then reopen VS Code:

```powershell
code .
```

---

# Troubleshooting

## Problem 1 — `winget` is not recognized

You may be using an older Windows installation or an outdated App Installer.

Install or update **App Installer** from the Microsoft Store.

Then reopen PowerShell.

---

## Problem 2 — `git` is not recognized

Close PowerShell and open it again.

Then run:

```powershell
git --version
```

If it still fails, reinstall Git:

```powershell
winget install -e --id Git.Git
```

---

## Problem 3 — `python` is not recognized

Close PowerShell and open it again.

Then try:

```powershell
python --version
```

If that fails:

```powershell
py --version
```

Tell the instructor if only `py` works.

---

## Problem 4 — PowerShell says running scripts is disabled

Run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Problem 5 — VS Code cannot find the Python environment

Press:

```text
Ctrl + Shift + P
```

Search for:

```text
Python: Select Interpreter
```

Choose the interpreter ending in:

```text
.venv\Scripts\python.exe
```

Then return to the notebook and select the same kernel.

---

## Problem 6 — A package is missing

Make sure the PowerShell prompt begins with:

```text
(.venv)
```

Then run:

```powershell
python -m pip install -r requirements.txt
```

---

## Problem 7 — The notebook says it cannot find the data folder

Make sure you opened VS Code from the repository root:

```powershell
cd $HOME\Desktop\afec-x-ai-workshop-2026
code .
```

Do not open only the `notebooks` folder as a separate project.

---

## Problem 8 — GitHub asks you to sign in

The repository may still be private.

Follow the instructor's instructions for GitHub access.

Once the repository is public, cloning will not require GitHub authentication.

---

# Quick setup summary

For a fresh Windows computer:

```powershell
winget install -e --id Git.Git
winget install -e --id Python.Python.3.11
winget install -e --id Microsoft.VisualStudioCode
```

Close and reopen PowerShell.

Then:

```powershell
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter

cd $HOME\Desktop

git clone https://github.com/cphanthian/afec-x-ai-workshop-2026.git
cd afec-x-ai-workshop-2026

python -m venv .venv

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

code .
```

Then open:

```text
notebooks/01_flower_kmeans_student.ipynb
```

and select the `.venv` Python kernel.

---

# Ready

If you can:

1. open the repository in VS Code;
2. open the `.ipynb` notebook;
3. select the `.venv` kernel; and
4. run the first code cell without an error,

then your computer is ready for the AFEC-X AI workshop.
