$ErrorActionPreference = "Stop"

Write-Host "AFEC-X AI Workshop 2026 setup" -ForegroundColor Cyan

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python was not found. Installing Python 3.11 with winget..."
    winget install -e --id Python.Python.3.11
    Write-Host ""
    Write-Host "Python has been installed. Close PowerShell, open it again, return to this repository, and run:"
    Write-Host "  .\setup_windows.ps1"
    exit
}

Write-Host "Python:"
python --version

if (-not (Test-Path ".venv")) {
    Write-Host "Creating .venv..."
    python -m venv .venv
}

Write-Host "Installing workshop packages..."
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt

Write-Host ""
Write-Host "Setup complete." -ForegroundColor Green
Write-Host "In VS Code, open notebooks\01_flower_kmeans_student.ipynb"
Write-Host "and select the .venv Python kernel."
