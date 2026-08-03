
# Class
import Src.Api.page as Page
from Src.Api.film import main_dw_film as download_film
from Src.Api.tv import main_dw_tv as download_tv
from Src.Util.message import msg_start
from Src.Util.console import console, msg
from Src.Util.os import remove_folder
from Src.Util.selection import ask_selection
from Src.Util.i18n import t, load_language, set_language, get_language, SUPPORTED_LANGUAGES, LANGUAGE_NAMES
from Src.Util.history import add_search, add_download, get_recent_searches, get_recent_downloads
from Src.Lib.FFmpeg.installer import check_ffmpeg

# Import
import sys
from rich.table import Table

try:
    import msvcrt
except ImportError:
    msvcrt = None

# [ util ]
def press_any_key(text=None):
    console.print(text if text is not None else f"[muted]{t('app.press_any_key')}[/]")
    if msvcrt:
        msvcrt.getch()
    else:
        input()

# [ menu actions ]
def download_flow():

    console.print(f"[title]{t('download.init')}[/]")
    check_ffmpeg()
    domain, site_version = Page.load_domain()
    console.print()

    if not domain:
        return

    while True:
        console.rule(f"[title]{t('download.search.title')}[/]", style="muted")
        console.print(f"[muted]{t('selection.cancel_hint')}[/]")
        film_search = msg.ask(f"[prompt]{t('download.search.prompt')}[/]").strip()

        if film_search in ("", "0"):
            return

        add_search(film_search)
        db_title = Page.search(film_search, domain)
        console.print()

        if len(db_title) == 0:
            console.print(f"[error]{t('download.search.empty')}[/]")
            console.print()
            continue

        Page.display_search_results(db_title)
        console.print()
        console.print(f"[info]{t('download.search.help1')}[/]")
        console.print(f"[muted]{t('download.search.help2')}[/]")
        console.print(f"[muted]{t('selection.cancel_hint')}[/]")
        selected_indexes = ask_selection(f"[prompt]{t('download.index_prompt')}[/]", len(db_title))

        if selected_indexes is None:
            console.print()
            continue

        for n in selected_indexes:
            selected_title = db_title[n - 1]

            console.print()
            console.rule(style="muted")

            if selected_title['type'] == "movie":
                console.print(f"[title]{t('download.movie_selected')}[/] [value]{selected_title['name']}[/]")
                download_film(selected_title['id'], selected_title['slug'], domain)
                add_download(selected_title['name'])
            else:
                console.print(f"[title]{t('download.tv_selected')}[/] [value]{selected_title['name']}[/]")
                completed = download_tv(selected_title['id'], selected_title['slug'], site_version, domain)
                if completed:
                    add_download(selected_title['name'])

        console.print()
        console.print(f"[success]{t('download.completed')}[/]")
        return

def language_flow():
    console.print(f"[info]{t('settings.language.current')}:[/] [value]{LANGUAGE_NAMES[get_language()]}[/]")
    console.print()

    for i, code in enumerate(SUPPORTED_LANGUAGES, start=1):
        marker = " *" if code == get_language() else ""
        console.print(f"[accent]{i}[/] [value]{LANGUAGE_NAMES[code]}{marker}[/]")

    console.print(f"[muted]{t('selection.cancel_hint')}[/]")
    chosen_index = ask_selection(f"[prompt]{t('settings.language.prompt')}[/]", len(SUPPORTED_LANGUAGES))

    if chosen_index is None:
        return

    chosen_code = SUPPORTED_LANGUAGES[chosen_index[0] - 1]
    set_language(chosen_code)

    console.print(f"[success]{t('settings.language.saved')}:[/] [value]{LANGUAGE_NAMES[chosen_code]}[/]")

def settings_flow():
    while True:
        console.rule(f"[title]{t('settings.title')}[/]", style="muted")
        console.print(f"[accent]1[/] [value]{t('settings.menu.domain')}[/]")
        console.print(f"[accent]2[/] [value]{t('settings.menu.language')}[/]")
        console.print(f"[accent]0[/] [value]{t('settings.menu.back')}[/]")
        choice = msg.ask(f"[prompt]{t('menu.choose_option')}[/]").strip()
        console.print()

        if choice == "1":
            Page.configure_domain()
            console.print()
            press_any_key()
        elif choice == "2":
            language_flow()
            console.print()
            press_any_key()
        elif choice == "0":
            return
        else:
            console.print(f"[error]{t('menu.invalid_option')}[/]")
            console.print()

def about_flow():
    console.rule(f"[title]{t('about.title')}[/]", style="muted")
    console.print(t("about.text1"))
    console.print(t("about.text2"))
    console.print(t("about.text3"))
    console.print()
    press_any_key()

def history_flow():
    console.rule(f"[title]{t('history.title')}[/]", style="muted")

    console.print(f"[title]{t('history.searches_title')}[/]")
    searches = get_recent_searches()
    if not searches:
        console.print(f"[muted]{t('history.empty')}[/]")
    else:
        table = Table(show_header=True, header_style="title", border_style="muted")
        table.add_column(t("table.when.col"), style="muted")
        table.add_column(t("table.query.col"), style="value")
        for entry in searches:
            table.add_row(entry["timestamp"], entry["text"])
        console.print(table)

    console.print()
    console.print(f"[title]{t('history.downloads_title')}[/]")
    downloads = get_recent_downloads()
    if not downloads:
        console.print(f"[muted]{t('history.empty')}[/]")
    else:
        table = Table(show_header=True, header_style="title", border_style="muted")
        table.add_column(t("table.when.col"), style="muted")
        table.add_column(t("table.title.col"), style="value")
        for entry in downloads:
            table.add_row(entry["timestamp"], entry["text"])
        console.print(table)

    console.print()
    press_any_key()

# [ menu ]
def show_menu():
    console.print(f"[title]{t('menu.title')}[/]")
    console.print(f"[accent]1[/] [value]{t('menu.option.download')}[/]")
    console.print(f"[accent]2[/] [value]{t('menu.option.settings')}[/]")
    console.print(f"[accent]3[/] [value]{t('menu.option.history')}[/]")
    console.print(f"[accent]4[/] [value]{t('menu.option.about')}[/]")

MENU_ACTIONS = {
    "1": download_flow,
    "2": settings_flow,
    "3": history_flow,
    "4": about_flow,
}

# [ main ]
def main():

    load_language()

    if sys.version_info < (3, 11):
        console.print(f"[error]{t('app.python_version_error')}[/]")
        sys.exit(0)

    remove_folder("tmp")
    msg_start()

    while True:
        show_menu()
        choice = msg.ask(f"[prompt]{t('menu.choose_option')}[/]").strip()
        console.print()

        action = MENU_ACTIONS.get(choice)
        if action is None:
            console.print(f"[error]{t('menu.invalid_option')}[/]")
            console.print()
            continue

        action()

        console.print()
        console.rule(style="muted")
        console.print()

if __name__ == '__main__':
    main()
