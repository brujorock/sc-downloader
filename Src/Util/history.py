# Tracks recent searches and successfully completed downloads, persisted to
# history.json. Only the most recent MAX_STORED entries per list are kept on
# disk; callers typically display just the last DISPLAY_LIMIT of those.

import json
from datetime import datetime

HISTORY_FILE = "history.json"
MAX_STORED = 50
DISPLAY_LIMIT = 10


def _load():
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.setdefault("searches", [])
    data.setdefault("downloads", [])
    return data


def _save(data):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


def _add(list_name, text):
    data = _load()
    data[list_name].append({
        "text": text,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    data[list_name] = data[list_name][-MAX_STORED:]
    _save(data)


def add_search(term):
    _add("searches", term)


def add_download(title):
    _add("downloads", title)


def get_recent_searches(limit=DISPLAY_LIMIT):
    return list(reversed(_load()["searches"][-limit:]))


def get_recent_downloads(limit=DISPLAY_LIMIT):
    return list(reversed(_load()["downloads"][-limit:]))
