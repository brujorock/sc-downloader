# 10.12.23

# Class import
from Src.Util.headers import get_headers
from Src.Util.console import console
from Src.Util.i18n import t

# General import
import requests, sys, json
from bs4 import BeautifulSoup
from rich.prompt import Confirm
from rich.table import Table

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
        domain = console.input(f"[prompt]{t('domain.prompt')}[/]").strip()
        domain = domain.replace("https://", "").replace("http://", "").rstrip("/")

        if not domain:
            console.print(f"[error]{t('domain.empty')}[/]")
            continue

        console.print(f"[info]{t('domain.testing')}[/] [value]{domain}[/]")
        version = test_domain(domain)

        if version:
            console.print(f"[success]{t('domain.working')}[/] [value]{domain}[/]")
            return domain, version
        else:
            console.print(f"[error]{t('domain.invalid')}[/]")

def load_domain():
    """Read-only: load the saved domain and verify it still works. Does not prompt or save. Used by the download flow."""

    try:
        with open('data.json', 'r') as file:
            req_repo = json.load(file)
    except FileNotFoundError:
        req_repo = {"domain": ""}

    saved_domain = req_repo.get('domain')

    if not saved_domain:
        console.print(f"[error]{t('domain.not_configured')}[/]")
        return None, None

    console.print(f"[info]{t('domain.checking')}[/]", end=" ")
    version = test_domain(saved_domain)

    if version:
        console.print(f"[success]✓ {t('domain.check_passed')}[/]")
        return saved_domain, version

    console.print(f"[error]✗ {t('domain.check_failed')}[/]")
    console.print(t("domain.saved_broken", domain=saved_domain))
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
        console.print(f"[info]{t('domain.current_saved')}[/] [value]{current_domain}[/]")
        if not Confirm.ask(f"[prompt]{t('domain.change_prompt')}[/]", default=False, console=console):
            console.print(f"[success]{t('domain.confirmed')}[/] [value]{current_domain}[/]")
            return

    domain, version = ask_new_domain()
    req_repo['domain'] = domain
    with open('data.json', 'w') as file:
        json.dump(req_repo, file)

    console.print(f"[success]{t('domain.saved')}[/] [value]{domain}[/]")

def search(title_search, domain):

    req = requests.get(f"https://{domain}/it/search", params={'q': title_search}, headers={'user-agent': get_headers()})

    if req.ok:
        try:
            soup = BeautifulSoup(req.text, "lxml")
            data_page = json.loads(soup.find("div", {"id": "app"}).get("data-page"))
            titles = data_page['props']['titles']
        except Exception:
            # Unexpected page (e.g. a challenge/error page served with a 200
            # status): treat it the same as "no results" so the search prompt
            # just re-asks instead of crashing the whole app.
            return []

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
        console.log(f"[error]{t('error.generic', status=req.status_code)}[/]")
        sys.exit(0)

def display_search_results(db_title):
    type_labels = {'movie': t('type.movie'), 'tv': t('type.tv')}

    table = Table(show_header=True, header_style="title", border_style="muted")
    table.add_column("#", style="accent", justify="right")
    table.add_column(t("table.title.col"), style="value")
    table.add_column(t("table.year.col"), style="muted", justify="center")
    table.add_column(t("table.type.col"), style="info")

    for i, title in enumerate(db_title, start=1):
        table.add_row(
            str(i),
            title['name'],
            title.get('year') or "-",
            type_labels.get(title['type'], title['type'])
        )

    console.print(table)
