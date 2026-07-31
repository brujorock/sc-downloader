# 13.09.2023

# Class import
from Src.Util.console import console

# General import
import os, requests, time

# Variable
repo_name = "StreamingCommunity_api"
repo_user = "ghost6446"
main = os.path.abspath(os.path.dirname(__file__))
base = "\\".join(main.split("\\")[:-1])

def get_install_version():
    about = {}
    with open(os.path.join(main, '__version__.py'), 'r', encoding='utf-8') as f:
        exec(f.read(), about)
    return about['__version__']

def main_update():
    console.print("[info]Verifica versione github in corso...[/]")

    json = requests.get(f"https://api.github.com/repos/{repo_user}/{repo_name}/releases").json()[0]
    stargazers_count = requests.get(f"https://api.github.com/repos/{repo_user}/{repo_name}").json()['stargazers_count']

    last_version = json['name']
    down_count = json['assets'][0]['download_count']

    if down_count > 0 and stargazers_count > 0:
        percentual_stars = round(stargazers_count / down_count * 100, 2)
    else:
        percentual_stars = 0

    if get_install_version() != last_version:
        console.print(f"[warning]E' disponibile una nuova versione:[/] [value]{json['zipball_url']}[/]")
        console.print(f"[info]Versione:[/] [value]{json['name']}[/]")
    else:
        console.print("[success]Tutto aggiornato[/]")
        console.print(f"[info]Ultima versione:[/] [value]{json['name']}[/]")

    console.print()
    console.print(f"[muted]{repo_name} e' stato scaricato {down_count} volte, ma solo il {percentual_stars}% di voi(!!) ha messo una stella.\n"
                   f"Aiuta la crescita del repository oggi, lasciando una stella e condividendolo con altri online![/]")
    time.sleep(2.5)
    console.print()