## SCDownloader by BarbieGirl♥

## Overview.
This repository provide a simple script designed to facilitate the downloading of films and series from a popular streaming community platform. The script allows users to download individual films, entire series, or specific episodes, providing a seamless experience for content consumers.

This is a fork of the original [Streaming Community downloader](https://github.com/Ghost6446/StreamingCommunity_api), rewritten with an interactive menu and a Barbie-themed CLI.

## Requirement
Make sure you have the following prerequisites installed on your system:

* python > [3.11](https://www.python.org/downloads/)
* ffmpeg [win](https://www.gyan.dev/ffmpeg/builds/)

## Installation library
Install the required Python libraries using the following command:
```bash
pip install -r requirements.txt
```

## Usage
Double-click `SCDownloader.bat` (Windows) to launch the app — it runs the venv's Python automatically, no manual activation needed.

Or run it manually with the venv activated:
```python
python run.py
```
You'll get an interactive menu:
1. **Scarica film o serie TV** — search and download (requires a domain to be configured first, see option 2).
2. **Impostazioni** — set or change the streaming domain used to search/download. Required before your first download.
3. **About SCD** — info about the project.

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

- Output layout: films go to `downloads/film/[nome film]/`, with subtitles in a `subtitle/` subfolder next to the video. TV episodes go to `downloads/tv/[nome serie]/`.

## Disclaimer
This project is for educational purposes only. Anyone downloading copyrighted or otherwise illegal content through it is solely responsible for their own actions.

## Authors
- [@brujorock](https://github.com/brujorock)
