## SCDownloader by BarbieGirl♥

## Overview
This repository provides a simple script designed to facilitate the downloading of films and series from a popular streaming community platform. The script allows users to download individual films, entire series, or specific episodes, providing a seamless experience for content consumers.

## Requirements
Works on **Windows**, **macOS** (Intel and Apple Silicon), and **Linux**. Make sure you have the following prerequisites installed on your system:

* python > [3.11](https://www.python.org/downloads/)
* ffmpeg:
  - **Windows**: if it's missing, the app offers to download and install it automatically on first run.
  - **macOS**: install via [Homebrew](https://brew.sh) — `brew install ffmpeg`. If the app doesn't find it, it will print these exact instructions (including how to install Homebrew itself if needed) and how to install ffmpeg.
  - **Linux**: install via your distribution's package manager, e.g. `sudo apt install ffmpeg`.

## Installation
Install the required Python libraries using the following command:
```bash
pip install -r requirements.txt
```

## Usage
- **Windows**: double-click `SCDownloader.bat` to launch the app — it runs the venv's Python automatically, no manual activation needed.
- **macOS/Linux**: double-click `SCDownloader.command` (or run `./SCDownloader.command` from Terminal) for the same one-click experience.

Or run it manually with the venv activated:
```python
python run.py
```
You'll get an interactive menu:
1. **Download a movie or TV series** — search and download (requires a domain to be configured first, see option 2).
2. **Settings** — configure the streaming domain and the interface language.
3. **Search & download history** — browse your most recent searches and completed downloads.
4. **About SCD** — info about the project.

## Language
The app is available in **English** (default), **Italian**, and **Spanish**. Change it anytime from `Settings -> Language` — the switch applies immediately and is remembered for future runs.

## Auto Update
Keep your script up to date with the latest features by running:
```python
python update.py
```

## Features
- Download Single Film: Easily download individual movies with a simple command.

- Download Specific Episodes or Entire Series: Seamlessly retrieve specific episodes or entire series using intuitive commands. Specify a range of episodes with square brackets notation, e.g., [5-7], or download all episodes with an asterisk (*).

- Sync Audio and Video: Ensure perfect synchronization between audio and video during the download process for an enhanced viewing experience.

- Subtitles: automatically downloads Italian, English and Spanish subtitles (when available), skipping every other language.

- Resilient downloads: failed segments are retried automatically with backoff, and you're warned clearly if a download ends up incomplete after all attempts.

- Output layout: films go to `downloads/film/[movie name]/`, with subtitles in a `subtitle/` subfolder next to the video. TV episodes go to `downloads/tv/[show name]/`.

## Disclaimer
This project is for educational purposes only. Anyone downloading copyrighted or otherwise illegal content through it is solely responsible for their own actions.

## Authors
- [@brujorock](https://github.com/brujorock)
