@echo off
title Educational Virus & Antivirus Launcher
color 0A
echo.
echo ============================================================
echo   EDUCATIONAL VIRUS & ANTIVIRUS - LAUNCHER
echo ============================================================
echo.
echo Starting launcher...
echo.

REM Try python first, then py (common on Windows)
python scripts\run.py
if errorlevel 1 (
    echo.
    echo Python command failed, trying 'py' instead...
    echo.
    py scripts\run.py
    if errorlevel 1 (
        echo.
        echo ============================================================
        echo ERROR: Python not found!
        echo ============================================================
        echo.
        echo Please make sure Python is installed.
        echo Try running: python scripts\run.py
        echo Or: py scripts\run.py
        echo.
        pause
        exit /b 1
    )
)

echo.
echo ============================================================
echo Program finished.
echo ============================================================
pause

