@echo off

cd /d "%~dp0"

echo Running "bb-fill-memory.py"...

if not exist ".venv" (
    echo .venv not found. Creating virtual environment...

    python -m venv .venv
    .venv\Scripts\pip.exe install -r requirements.txt
)

.venv\Scripts\python.exe bb-fill-memory.py

echo.
echo Application exited.
pause