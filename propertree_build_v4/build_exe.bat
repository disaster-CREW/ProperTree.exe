@echo off
setlocal enabledelayedexpansion

REM ================================================
REM  Build ProperTree.exe (windowed, no console)
REM ================================================

echo ================================================
echo   ProperTree .exe Builder
echo ================================================
echo.

:CHECK_PYTHON
REM Check for Python in PATH
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python was not found in your system PATH.
    echo.
    set /p "USER_INPUT=Please paste the full path to python.exe: "
    
    REM Strip any quotes the user might have pasted
    set "USER_INPUT=!USER_INPUT:"=!"
    
    if not exist "!USER_INPUT!" (
        echo.
        echo ERROR: "!USER_INPUT!" is an invalid path.
        pause
        goto CHECK_PYTHON
    )
    
    set "PYTHON_CMD="!USER_INPUT!""
    set "PIP_CMD="!USER_INPUT!" -m pip"
) else (
    set "PYTHON_CMD=python"
    set "PIP_CMD=pip"
)

REM Install PyInstaller if not present
echo.
echo [1/3] Installing PyInstaller...
%PIP_CMD% install pyinstaller --quiet
if errorlevel 1 (
    echo ERROR: Failed to install PyInstaller.
    pause
    exit /b 1
)

REM Change to script directory
cd /d "%~dp0"

REM Build using the spec file
echo.
echo [2/3] Building ProperTree.exe (this may take a minute)...
%PYTHON_CMD% -m PyInstaller ProperTree.spec --noconfirm
if errorlevel 1 (
    echo.
    echo ERROR: Build failed. See errors above.
    pause
    exit /b 1
)

echo.
echo [3/3] Build complete!
echo.
echo Your ProperTree.exe is located at:
echo   %~dp0dist\ProperTree\ProperTree.exe
echo.
pause

