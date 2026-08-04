@echo off
title SCDownloader - Update
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo [ERRORE] Ambiente virtuale non trovato in .venv\
    echo Crealo con:  python -m venv .venv
    echo Poi installa le dipendenze con:  .venv\Scripts\pip install -r requirements.txt
    pause
    exit /b 1
)

".venv\Scripts\python.exe" update.py

pause
