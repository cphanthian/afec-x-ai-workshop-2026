# AFEC-X 2026 — Student Setup Manual for macOS

This guide is for students who are starting from **zero** on a Mac.

You do **not** need prior Python experience.

By the end of this setup, you will be able to:

- install the required tools;
- download the workshop repository;
- create an isolated Python environment;
- install the workshop packages;
- open and run the Jupyter Notebook in VS Code.

---

# 1. What you need

You need:

- a Mac running a reasonably recent version of macOS;
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

This setup works on both Apple silicon and Intel Macs.

---

# 2. Open Terminal

Press:

```text
Command + Space
```

Type:

```text
Terminal
```

and press Enter.

You should see a prompt similar to:

```text
yourname@MacBook ~ %
```

All commands in this manual should be entered into Terminal unless stated otherwise.

---

# 3. Install Homebrew

First check whether Homebrew is already installed:

```bash
brew --version
```

If a version number appears, continue to the next step.

If `brew` is not found, install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the instructions shown in Terminal.

At the end, Homebrew may show one or two commands that add Homebrew to your shell PATH. Copy and run those commands exactly if prompted.

Then close Terminal, open it again, and check:

```bash
brew --version
```

---

# 4. Install Git

Run:

```bash
brew install git
```

Check:

```bash
git --version
```

You should see something similar to:

```text
git version 2.x.x
```

---

# 5. Install Python 3.11

Run:

```bash
brew install python@3.11
```

Check:

```bash
python3.11 --version
```

Expected output:

```text
Python 3.11.x
```

For this workshop, use `python3.11` when creating the virtual environment.

---

# 6. Install Visual Studio Code

Run:

```bash
brew install --cask visual-studio-code
```

After installation, open VS Code from the Applications folder.

---

# 7. Enable the `code` command

On macOS, the `code` command may not be available automatically.

Open VS Code.

Press:

```text
Command + Shift + P
```

Search for:

```text
Shell Command: Install 'code' command in PATH
```

Run that command.

Then close Terminal and open it again.

Check:

```bash
code --version
```

If a version number appears, the command is ready.

---

# 8. Install the VS Code Python and Jupyter extensions

Run:

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
```

---

# 9. Go to your Desktop

Run:

```bash
cd ~/Desktop
```

Check:

```bash
pwd
```

The path should end in:

```text
Desktop
```

---

# 10. Download the workshop repository

Run:

```bash
git clone https://github.com/cphanthian/afec-x-ai-workshop-2026.git
```

Then enter the repository:

```bash
cd afec-x-ai-workshop-2026
```

Check the files:

```bash
ls
```

You should see files and folders such as:

```text
README.md
requirements.txt
data
notebooks
scripts
```

---

# 11. Create a Python virtual environment

Run:

```bash
python3.11 -m venv .venv
```

This creates a folder called:

```text
.venv
```

inside the workshop repository.

---

# 12. Activate the virtual environment

Run:

```bash
source .venv/bin/activate
```

If successful, the Terminal prompt should begin with:

```text
(.venv)
```

For example:

```text
(.venv) yourname@MacBook afec-x-ai-workshop-2026 %
```

---

# 13. Install the workshop packages

First update pip:

```bash
python -m pip install --upgrade pip
```

Then install the workshop requirements:

```bash
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

---

# 14. Check the environment

Run:

```bash
python -c "import sys; print(sys.executable)"
```

The output should end in something similar to:

```text
afec-x-ai-workshop-2026/.venv/bin/python
```

Then test the main packages:

```bash
python -c "import numpy, matplotlib, PIL, sklearn; print('Workshop environment OK')"
```

Expected output:

```text
Workshop environment OK
```

---

# 15. Open the workshop in VS Code

Run:

```bash
code .
```

VS Code should open the repository.

---

# 16. Open the Jupyter Notebook

In the VS Code Explorer, open:

```text
notebooks
└── 01_flower_kmeans_student.ipynb
```

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

Then select the environment whose path contains:

```text
.venv/bin/python
```

Do not select another Python installation if the `.venv` environment is available.

---

# 18. Test the notebook

Run the first Python code cell.

If the imports run without an error, your environment is ready.

---

# 19. Workshop dataset

The final workshop repository will contain datasets under:

```text
data/
├── supervised/
└── unsupervised/
```

For the supervised-learning activity, the butterfly images are used in Teachable Machine.

For the unsupervised-learning activity, the notebook reads flower images from:

```text
data/unsupervised/flowers/
```

---

# 20. The next time you open the workshop

You do **not** need to reinstall Python or the packages.

Open Terminal and run:

```bash
cd ~/Desktop/afec-x-ai-workshop-2026
source .venv/bin/activate
code .
```

Then open the notebook and select the `.venv` kernel if VS Code does not select it automatically.

---

# 21. Updating the workshop files

If the instructor tells you that the repository has been updated, run:

```bash
cd ~/Desktop/afec-x-ai-workshop-2026
git pull
```

Then reopen VS Code:

```bash
code .
```

---

# Troubleshooting

## Problem 1 — `brew` is not recognized

Homebrew may not yet be in your shell PATH.

Reopen Terminal and try:

```bash
brew --version
```

If it still fails, rerun the Homebrew installer and follow the PATH instructions printed at the end.

---

## Problem 2 — Git asks to install developer tools

macOS may display a prompt for Command Line Developer Tools.

Allow the installation to complete, then run:

```bash
git --version
```

again.

---

## Problem 3 — `python3.11` is not recognized

Check whether Homebrew installed it:

```bash
brew list python@3.11
```

Then try:

```bash
$(brew --prefix python@3.11)/bin/python3.11 --version
```

If that works, create the environment with:

```bash
$(brew --prefix python@3.11)/bin/python3.11 -m venv .venv
```

---

## Problem 4 — `code` is not recognized

Open VS Code.

Press:

```text
Command + Shift + P
```

Run:

```text
Shell Command: Install 'code' command in PATH
```

Close Terminal, open it again, and try:

```bash
code --version
```

---

## Problem 5 — VS Code cannot find the virtual environment

Press:

```text
Command + Shift + P
```

Search for:

```text
Python: Select Interpreter
```

Choose the interpreter ending in:

```text
.venv/bin/python
```

Then return to the notebook and select the same kernel.

---

## Problem 6 — A Python package is missing

Activate the environment:

```bash
source .venv/bin/activate
```

Then run:

```bash
python -m pip install -r requirements.txt
```

---

## Problem 7 — The notebook cannot find the data folder

Make sure VS Code was opened from the repository root:

```bash
cd ~/Desktop/afec-x-ai-workshop-2026
code .
```

Do not open only the `notebooks` folder as a separate project.

---

# Quick setup summary

For a fresh Mac:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install git
brew install python@3.11
brew install --cask visual-studio-code
```

Open VS Code once and run:

```text
Command + Shift + P
→ Shell Command: Install 'code' command in PATH
```

Then open a new Terminal:

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter

cd ~/Desktop

git clone https://github.com/cphanthian/afec-x-ai-workshop-2026.git
cd afec-x-ai-workshop-2026

python3.11 -m venv .venv
source .venv/bin/activate

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

then your Mac is ready for the AFEC-X AI workshop.
