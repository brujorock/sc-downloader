# 10.12.23

# Class import
from Src.Util.headers import get_headers
from Src.Util.console import console

# General import
import requests, sys, json
from bs4 import BeautifulSoup
from rich.prompt import Confirm
from rich.table import Table

TYPE_LABELS = {'movie': 'Film', 'tv': 'Serie TV'}

def test_domain(domain):
    """Try to reach the domain and read its site version. Returns the version string, or None if unreachable/invalid."""

    site_url = f"https://{domain}"
    try:
        site_request = requests.get(site_url, headers={'user-agent': get_headers()}, timeout=10)
        soup = BeautifulSoup(site_request.text, "lxml")
        return json.loads(soup.find("div", {"id": "app"}).get("data-page"))['version']
    except Exception:
        return None

def ask_new_domain():
    """Ask the user for a domain and keep asking until one actually responds."""

    while True:
        domain = console.input("[prompt]Inserisci il dominio completo (es. streamingcommunity.report): [/]").strip()
        domain = domain.replace("https://", "").replace("http://", "").rstrip("/")

        if not domain:
            console.print("[error]Dominio vuoto, riprova.[/]")
            continue

        console.print(f"[info]Test dominio:[/] [value]{domain}[/]")
        version = test_domain(domain)

        if version:
            console.print(f"[success]Dominio funzionante:[/] [value]{domain}[/]")
            return domain, version
        else:
            console.print("[error]Il dominio inserito non risponde, non esiste o non e' scritto bene. Reinseriscilo.[/]")

def load_domain():
    """Read-only: load the saved domain and verify it still works. Does not prompt or save. Used by the download flow."""

    console.print("[info]Recupero regole in corso...[/]")

    try:
        with open('data.json', 'r') as file:
            req_repo = json.load(file)
    except FileNotFoundError:
        req_repo = {"domain": ""}

    saved_domain = req_repo.get('domain')

    if not saved_domain:
        console.print("[error]Nessun dominio configurato. Vai su[/] [value]Impostazioni[/] [error]per configurarlo.[/]")
        return None, None

    console.print(f"[info]Test dominio:[/] [value]{saved_domain}[/]")
    version = test_domain(saved_domain)

    if version:
        console.print(f"[success]Dominio funzionante:[/] [value]{saved_domain}[/]")
        return saved_domain, version

    console.print(f"[error]Il dominio salvato[/] [value]{saved_domain}[/] [error]non risponde piu'. Vai su[/] [value]Impostazioni[/] [error]per aggiornarlo.[/]")
    return None, None

def configure_domain():
    """Interactive: show the saved domain (if any) and let the user set or change it, then save it. Used by the settings menu."""

    try:
        with open('data.json', 'r') as file:
            req_repo = json.load(file)
    except FileNotFoundError:
        req_repo = {"domain": ""}

    current_domain = req_repo.get('domain')

    if current_domain:
        console.print(f"[info]Dominio attualmente salvato:[/] [value]{current_domain}[/]")
        if not Confirm.ask("[prompt]Vuoi cambiarlo?[/]", default=False, console=console):
            console.print(f"[success]Dominio confermato:[/] [value]{current_domain}[/]")
            return

    domain, version = ask_new_domain()
    req_repo['domain'] = domain
    with open('data.json', 'w') as file:
        json.dump(req_repo, file)

    console.print(f"[success]Dominio salvato:[/] [value]{domain}[/]")

def search(title_search, domain):

    req = requests.get(f"https://{domain}/it/search", params={'q': title_search}, headers={'user-agent': get_headers()})

    if req.ok:
        soup = BeautifulSoup(req.text, "lxml")
        data_page = json.loads(soup.find("div", {"id": "app"}).get("data-page"))
        titles = data_page['props']['titles']
        results = []
        for title in titles:
            release_date = title.get('last_air_date_it') or title.get('last_air_date')
            year = release_date[:4] if release_date else None
            results.append({
                'name': title['name'],
                'type': title['type'],
                'id': title['id'],
                'slug': title['slug'],
                'year': year
            })
        return results[0:21]
    else:
        console.log(f"[error]Errore: {req.status_code}[/]")
        sys.exit(0)

def display_search_results(db_title):
    table = Table(show_header=True, header_style="title", border_style="muted")
    table.add_column("#", style="accent", justify="right")
    table.add_column("Titolo", style="value")
    table.add_column("Anno", style="muted", justify="center")
    table.add_column("Tipo", style="info")

    for i, title in enumerate(db_title, start=1):
        table.add_row(
            str(i),
            title['name'],
            title.get('year') or "-",
            TYPE_LABELS.get(title['type'], title['type'])
        )

    console.print(table)
