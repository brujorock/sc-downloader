#!/bin/bash
cd "$(dirname "$0")"

if [ ! -f ".venv/bin/python3" ]; then
    echo "[ERRORE] Ambiente virtuale non trovato in .venv/"
    echo "Crealo con:  python3 -m venv .venv"
    echo "Poi installa le dipendenze con:  .venv/bin/pip install -r requirements.txt"
    read -n 1 -s -r -p "Premi un tasto per uscire..."
    echo
    exit 1
fi

.venv/bin/python3 update.py

read -n 1 -s -r -p "Premi un tasto per uscire..."
echo
