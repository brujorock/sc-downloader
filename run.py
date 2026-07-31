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

# [ main ]
def initialize():

    if sys.version_info < (3, 11):
        console.print("[error]Installa una versione di Python > 3.11[/]")
        sys.exit(0)

    remove_folder("tmp")
    msg_start()
    check_ffmpeg()
    console.print()

def main():

    initialize()
    domain, site_version = Page.domain_version()
    console.print()

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

if __name__ == '__main__':
    main()
