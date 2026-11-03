#!/bin/bash

set -e

echo "========================================"
echo "AFEC-X AI Workshop 2026 — macOS Setup"
echo "========================================"
echo

# ------------------------------------------------------------
# 1. Check Homebrew
# ------------------------------------------------------------

if ! command -v brew >/dev/null 2>&1; then
    echo "Homebrew was not found."
    echo
    echo "Install Homebrew first with:"
    echo
    echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
    echo
    echo "Then close Terminal, open it again, return to this repository,"
    echo "and run:"
    echo
    echo "  bash setup_macos.sh"
    echo
    exit 1
fi

echo "Homebrew:"
brew --version | head -n 1
echo


# ------------------------------------------------------------
# 2. Check Git
# ------------------------------------------------------------

if ! command -v git >/dev/null 2>&1; then
    echo "Git was not found. Installing Git..."
    brew install git
fi

echo "Git:"
git --version
echo


# ------------------------------------------------------------
# 3. Check / install Python 3.11
# ------------------------------------------------------------

if ! command -v python3.11 >/dev/null 2>&1; then
    echo "Python 3.11 was not found."
    echo "Installing Python 3.11 with Homebrew..."
    brew install python@3.11
fi

PYTHON_BIN="$(command -v python3.11 || true)"

if [ -z "$PYTHON_BIN" ]; then
    PYTHON_BIN="$(brew --prefix python@3.11)/bin/python3.11"
fi

if [ ! -x "$PYTHON_BIN" ]; then
    echo "Python 3.11 could not be found after installation."
    echo "Please check your Homebrew installation."
    exit 1
fi

echo "Python:"
"$PYTHON_BIN" --version
echo


# ------------------------------------------------------------
# 4. Check VS Code
# ------------------------------------------------------------

if ! command -v code >/dev/null 2>&1; then

    if [ -d "/Applications/Visual Studio Code.app" ]; then
        echo "VS Code is installed, but the 'code' command is not available."
        echo
        echo "Open VS Code, press Command + Shift + P, then run:"
        echo
        echo "  Shell Command: Install 'code' command in PATH"
        echo
        echo "You can continue setup now. The Python environment will still be created."
        echo

    else
        echo "VS Code was not found."
        echo "Installing Visual Studio Code..."
        brew install --cask visual-studio-code
        echo
        echo "After installation, open VS Code once."
        echo "Then press Command + Shift + P and run:"
        echo
        echo "  Shell Command: Install 'code' command in PATH"
        echo
    fi
fi


# ------------------------------------------------------------
# 5. Create virtual environment
# ------------------------------------------------------------

if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment (.venv)..."
    "$PYTHON_BIN" -m venv .venv
else
    echo "Existing .venv found. Reusing it."
fi

echo


# ------------------------------------------------------------
# 6. Install dependencies
# ------------------------------------------------------------

echo "Updating pip..."
./.venv/bin/python -m pip install --upgrade pip

echo
echo "Installing workshop packages..."
./.venv/bin/python -m pip install -r requirements.txt

echo


# ------------------------------------------------------------
# 7. Optional VS Code extensions
# ------------------------------------------------------------

if command -v code >/dev/null 2>&1; then
    echo "Installing VS Code Python and Jupyter extensions..."
    code --install-extension ms-python.python --force
    code --install-extension ms-toolsai.jupyter --force
    echo
fi


# ------------------------------------------------------------
# 8. Quick environment test
# ------------------------------------------------------------

echo "Testing workshop environment..."

./.venv/bin/python -c "import numpy, matplotlib, PIL, sklearn; print('Workshop environment OK')"

echo


# ------------------------------------------------------------
# 9. Done
# ------------------------------------------------------------

echo "========================================"
echo "Setup complete"
echo "========================================"
echo
echo "To activate the environment manually:"
echo
echo "  source .venv/bin/activate"
echo
echo "Then open VS Code:"
echo
echo "  code ."
echo
echo "Open:"
echo
echo "  notebooks/01_flower_kmeans_student.ipynb"
echo
echo "and select the Python kernel from:"
echo
echo "  .venv/bin/python"
echo

if ! command -v code >/dev/null 2>&1; then
    echo "Note:"
    echo "The 'code' command is still unavailable."
    echo "Open VS Code manually and install the shell command from the Command Palette."
fi
