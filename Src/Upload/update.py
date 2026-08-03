# 13.09.2023

# Class import
from Src.Util.console import console
from Src.Util.i18n import t

# General import
import os, requests, time

# Variable
repo_name = "sc-downloader"
repo_user = "brujorock"
main = os.path.abspath(os.path.dirname(__file__))
base = "\\".join(main.split("\\")[:-1])

def get_install_version():
    about = {}
    with open(os.path.join(main, '__version__.py'), 'r', encoding='utf-8') as f:
        exec(f.read(), about)
    return about['__version__']

def main_update():
    console.print(f"[info]{t('update.checking')}[/]")

    json = requests.get(f"https://api.github.com/repos/{repo_user}/{repo_name}/releases").json()[0]
    stargazers_count = requests.get(f"https://api.github.com/repos/{repo_user}/{repo_name}").json()['stargazers_count']

    last_version = json['name']
    down_count = json['assets'][0]['download_count']

    if down_count > 0 and stargazers_count > 0:
        percentual_stars = round(stargazers_count / down_count * 100, 2)
    else:
        percentual_stars = 0

    if get_install_version() != last_version:
        console.print(f"[warning]{t('update.new_version')}[/] [value]{json['zipball_url']}[/]")
        console.print(f"[info]{t('update.version_label')}[/] [value]{json['name']}[/]")
    else:
        console.print(f"[success]{t('update.up_to_date')}[/]")
        console.print(f"[info]{t('update.latest_version')}[/] [value]{json['name']}[/]")

    console.print()
    console.print(f"[muted]{t('update.stats', repo=repo_name, count=down_count, percent=percentual_stars)}[/]")
    time.sleep(2.5)
    console.print()