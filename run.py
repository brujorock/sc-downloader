# 10.12.23 -> 31.01.24

# Class
import Src.Api.page as Page
from Src.Api.film import main_dw_film as download_film
from Src.Api.tv import main_dw_tv as download_tv
from Src.Util.message import msg_start
from Src.Util.console import console, msg
from Src.Util.os import remove_folder
from Src.Util.selection import ask_selection
from Src.Lib.FFmpeg.installer import check_ffmpeg

# Import
import sys

try:
    import msvcrt
except ImportError:
    msvcrt = None

# [ util ]
def press_any_key(text="[muted]Premi un tasto qualsiasi per tornare al menu principale...[/]"):
    console.print(text)
    if msvcrt:
        msvcrt.getch()
    else:
        input()

# [ menu actions ]
def download_flow():

    console.print("[title]Inizializzazione:[/]")
    check_ffmpeg()
    domain, site_version = Page.load_domain()
    console.print()

    if not domain:
        return

    console.rule("[title]Ricerca[/]", style="muted")
    film_search = msg.ask("[prompt]Inserisci una parola da cercare nel sito[/]").strip()
    db_title = Page.search(film_search, domain)
    console.print()

    if len(db_title) == 0:
        console.print("[error]Nessun elemento trovato.[/]")
        return

    Page.display_search_results(db_title)
    console.print()
    console.print(
        "[info]Inserisci il [value]numero[/] indice, [value][1-2][/] per un intervallo, "
        "[value][1,3,5][/] per titoli non consecutivi.[/]"
    )
    console.print("[muted]Per le serie TV potrai scegliere anche stagione ed episodio da scaricare.[/]")
    selected_indexes = ask_selection("[prompt]Indice da scaricare[/]", len(db_title))

    for n in selected_indexes:
        selected_title = db_title[n - 1]

        console.print()
        console.rule(style="muted")

        if selected_title['type'] == "movie":
            console.print(f"[title]Film selezionato:[/] [value]{selected_title['name']}[/]")
            download_film(selected_title['id'], selected_title['slug'], domain)
        else:
            console.print(f"[title]Serie TV selezionata:[/] [value]{selected_title['name']}[/]")
            download_tv(selected_title['id'], selected_title['slug'], site_version, domain)

    console.print()
    console.print("[success]Completato.[/]")

def settings_flow():
    console.rule("[title]Impostazioni[/]", style="muted")
    Page.configure_domain()
    console.print()
    press_any_key()

def about_flow():
    console.rule("[title]About SCD[/]", style="muted")
    console.print(
        "[info]Streaming Community Downloader e' stato creato da[/] [value]BarbieGirl♥[/] [info]nel 2026, "
        "per puro scopo didattico.[/]"
    )
    console.print("[info]Non ha fini di lucro e puo' essere scaricato, modificato e utilizzato da chiunque.[/]")
    console.print(
        "[warning]Chi lo utilizza per scaricare materiale protetto da copyright o comunque illegale "
        "se ne assume la piena responsabilita'.[/]"
    )
    console.print()
    press_any_key()

# [ menu ]
def show_menu():
    console.print("[title]Menu:[/]")
    console.print("[accent]1[/] [value]Scarica film o serie TV[/]")
    console.print("[accent]2[/] [value]Impostazioni[/]")
    console.print("[accent]3[/] [value]About SCD[/]")

MENU_ACTIONS = {
    "1": download_flow,
    "2": settings_flow,
    "3": about_flow,
}

# [ main ]
def main():

    if sys.version_info < (3, 11):
        console.print("[error]Installa una versione di Python > 3.11[/]")
        sys.exit(0)

    remove_folder("tmp")
    msg_start()

    while True:
        show_menu()
        choice = msg.ask("[prompt]Seleziona un'opzione[/]").strip()
        console.print()

        action = MENU_ACTIONS.get(choice)
        if action is None:
            console.print("[error]Opzione non valida.[/]")
            console.print()
            continue

        action()

        console.print()
        console.rule(style="muted")
        console.print()

if __name__ == '__main__':
    main()
