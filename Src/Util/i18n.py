# Central place for every user-facing string in the app, in every supported
# language. Nothing else in the project should hardcode display text — call
# t("some.key", **kwargs) instead, and add the string here once per language.
#
# Default language is English. The chosen language is persisted in data.json
# under the "language" key, alongside the saved domain.

import json

SUPPORTED_LANGUAGES = ["en", "it", "es"]
LANGUAGE_NAMES = {
    "en": "English",
    "it": "Italiano",
    "es": "Español",
}
DEFAULT_LANGUAGE = "en"

_current_language = DEFAULT_LANGUAGE

TRANSLATIONS = {
    "en": {
        # app / general
        "app.python_version_error": "Please install a Python version > 3.11",
        "app.press_any_key": "Press any key to return to the main menu...",
        "error.generic": "Error: {status}",

        # menu
        "menu.title": "Menu:",
        "menu.option.download": "Download a movie or TV series",
        "menu.option.settings": "Settings",
        "menu.option.history": "Search & download history",
        "menu.option.about": "About SCDownloader",
        "menu.choose_option": "Choose an option",
        "menu.invalid_option": "Invalid option.",

        # history
        "history.title": "Search & Download History",
        "history.searches_title": "Recent searches",
        "history.downloads_title": "Recent downloads",
        "history.empty": "No items to show.",
        "table.when.col": "When",
        "table.query.col": "Search term",

        # download flow
        "download.init": "Initialization:",
        "download.search.title": "Search",
        "download.search.prompt": "Enter a word to search across the site",
        "download.search.empty": "No results found.",
        "download.search.help1": "Enter an [value]index[/] number, [value][1-2][/] for a range, [value][1,3,5][/] for non-consecutive titles.",
        "download.search.help2": "For TV series you can also choose the season and episode to download.",
        "download.index_prompt": "Index to download",
        "download.movie_selected": "Selected movie:",
        "download.tv_selected": "Selected TV series:",
        "download.completed": "Download queue completed.",
        "download.summary_title": "Download summary",
        "download.status.success": "Downloaded",
        "download.status.failed": "Not downloaded",
        "download.retry_prompt": "Do you want to retry downloading the titles that failed?",

        # settings
        "settings.title": "Settings",
        "settings.menu.domain": "Domain",
        "settings.menu.language": "Language",
        "settings.menu.back": "Back to main menu",
        "settings.language.current": "Current language",
        "settings.language.prompt": "Choose a language",
        "settings.language.saved": "Language saved",

        # about
        "about.title": "About SCDownloader",
        "about.text1": "[info]SCDownloader was created by[/] [value]BarbieGirl♥[/] [info]in 2026, for purely educational purposes.[/]",
        "about.text2": "[info]It is non-profit and can be downloaded, modified and used by anyone.[/]",
        "about.text3": "[warning]Anyone using it to download copyrighted or otherwise illegal material assumes full responsibility for doing so.[/]",

        # domain
        "domain.prompt": "Enter the full domain (e.g. streamingcommunity.report): ",
        "domain.empty": "Empty domain, try again.",
        "domain.testing": "Testing domain:",
        "domain.working": "Working domain:",
        "domain.invalid": "The domain you entered doesn't respond, doesn't exist, or isn't written correctly. Try again.",
        "domain.loading_rules": "Fetching rules...",
        "domain.not_configured": "No domain configured. Go to [value]Settings[/] to set one up.",
        "domain.saved_broken": "[error]The saved domain[/] [value]{domain}[/] [error]no longer responds. Go to[/] [value]Settings[/] [error]to update it.[/]",
        "domain.current_saved": "Currently saved domain:",
        "domain.change_prompt": "Do you want to change it?",
        "domain.confirmed": "Domain confirmed:",
        "domain.saved": "Domain saved:",

        # search results table
        "table.title.col": "Title",
        "table.year.col": "Year",
        "table.type.col": "Type",
        "table.episode.col": "Ep.",
        "type.movie": "Movie",
        "type.tv": "TV Series",
        "common.yes": "yes",

        # tv
        "tv.no_valid_video": "Could not find a valid video quality in the playlist",
        "tv.download_episode": "Downloading episode:",
        "tv.audio_track_used": "Using m3u8 audio track:",
        "tv.seasons_found": "Seasons found:",
        "tv.season_help": "Enter the [value]number[/] of the season, [value](*)[/] for all seasons, [value][1-2][/] for a range.",
        "tv.season_prompt": "Season number",
        "tv.episode_help": "Enter the [value]number[/] of the episode, [value](*)[/] for all episodes, [value][1-2][/] for a range.",
        "tv.episode_prompt": "Episode number",

        # film
        "film.unavailable": "Unable to play this video (not available)",

        # m3u8 / downloader
        "m3u8.parse_error": "Error parsing M3U8 content: {error}",
        "m3u8.no_video_playlist": "No video playlist found",
        "m3u8.download_subtitle": "Downloading subtitle:",
        "m3u8.no_subtitle": "No subtitle found",
        "m3u8.found_audio_playlists": "Found {count} playlists with audio",
        "m3u8.no_audio_playlist": "Could not find a playlist with audio",
        "m3u8.invalid": "Invalid m3u8, error: {status}",
        "m3u8.task_error": "An error occurred: {error}",
        "m3u8.retry": "Attempt {attempt}/{max}: {count} failed segments (waiting {backoff}s)",
        "m3u8.progress.download": "Downloading",
        "m3u8.progress.retry": "Retrying",
        "m3u8.incomplete_title": "WARNING: incomplete download",
        "m3u8.incomplete_body1": "{failed} out of {total} segments were NOT downloaded after {max} attempts.",
        "m3u8.incomplete_body2": "The resulting file will have gaps/skips at those points.",
        "m3u8.no_progress": "No progress for {seconds} seconds.",
        "m3u8.breaking_pool": "Stopping the thread pool...",
        "m3u8.joining_files": "Joining all files together",
        "m3u8.save_error": "Error saving the MP4: {error}",
        "m3u8.cleaning": "Cleaning up...",
        "m3u8.download_video": "Downloading video segments",
        "m3u8.download_audio": "Downloading audio segments",
        "m3u8.merge_success": "Video file created successfully.",
        "m3u8.sync_mismatch_title": "WARNING: audio and video out of sync",
        "m3u8.sync_mismatch_body": "Video duration ({video}) and audio duration ({audio}) don't match closely enough — they're likely from different sources. Discarding this download.",
        "m3u8.merge_error": "Error merging audio/video: {error}",
        "m3u8.merge_kept_raw": "Raw video and audio kept at: {video} , {audio}",
        "m3u8.invalid_url": "Invalid URL, error: {status}",
        "m3u8.download_from_playlist": "Downloading m3u8 from the playlist",
        "m3u8.language_selected": "Language selected:",
        "m3u8.index_selected": "m3u8 index selected:",
        "m3u8.no_valid_index": "Could not find a valid m3u8 index",
        "m3u8.download_from_index": "Downloading m3u8 from the index:",

        # ffmpeg installer
        "ffmpeg.downloading": "Downloading FFmpeg...",
        "ffmpeg.checking": "Checking ffmpeg...",
        "ffmpeg.found": "Found",
        "ffmpeg.not_in_path": "FFmpeg is not in the PATH. Downloading and adding it to the PATH...",
        "ffmpeg.need_admin": "You need to be an administrator to proceed!",
        "ffmpeg.download_failed": "Unable to download or add FFmpeg to the PATH.",
        "ffmpeg.missing.title": "FFmpeg is required but was not found on your system.",
        "ffmpeg.missing.what": "FFmpeg is used to download and merge the video/audio files, so the app can't work without it.",
        "ffmpeg.missing.macos.brew_about": "On macOS the easiest way to install it is with Homebrew, the standard package manager for command-line tools.",
        "ffmpeg.missing.macos.brew_check": "You don't seem to have Homebrew yet. Install it by running this command in Terminal:",
        "ffmpeg.missing.macos.brew_install_ffmpeg": "Then install FFmpeg with:",
        "ffmpeg.missing.linux.hint": "Install it with your distribution's package manager, for example:",
        "ffmpeg.missing.retry": "Once it's installed, run this app again.",

        # duration
        "duration.error": "Error: {error}",
        "duration.label": "Duration",

        # selection parsing
        "selection.empty_brackets": "Invalid format: empty brackets.",
        "selection.invalid_list": "Invalid list format: '{text}'. Use [N,M,K] with whole numbers, e.g. [1,3,5].",
        "selection.invalid_range": "Invalid range format: '{text}'. Use [N-M], e.g. [1-2].",
        "selection.invalid_range_numbers": "Invalid range format: '{text}'. Use [N-M] with whole numbers, e.g. [1-2].",
        "selection.out_of_range_list": "Indexes out of range (1-{max}): {list}",
        "selection.invalid_format": "'{text}' is not a valid format. Use a number, '*' or [N-M] (e.g. [1-2]).",
        "selection.out_of_range": "Index out of range: must be between 1 and {max}.",
        "selection.retry_suffix": "Try again.",
        "selection.cancel_hint": "Enter [value]0[/] to go back.",

        # filesystem
        "fs.remove_folder_error": "Error removing folder '{path}': {error}",
        "fs.remove_file_error": "Error removing file '{path}': {error}",
        "fs.file_not_found": "File '{path}' does not exist.",

        # legacy update / upload scripts
        "update.checking": "Checking github version...",
        "update.new_version": "A new version is available:",
        "update.version_label": "Version:",
        "update.up_to_date": "Everything is up to date",
        "update.latest_version": "Latest version:",
        "update.stats": "{repo} has been downloaded {count} times, but only {percent}% of you(!!) have starred it.\nHelp the repository grow today by leaving a star and sharing it online!",
        "upload.invalid_dir": "Error: '{dir}' is not a valid directory.",
        "upload.permission_error": "Permission error: {error}. Check permissions and try running the script as administrator.",
        "upload.generic_error": "Error: {error}",
        "upload.requesting_repo": "Requesting the github repository",
        "upload.fetching_zip": "Fetching the zip file from the repository",
        "upload.extracting": "Extracting files...",
        "upload.commit_success": "Latest commit downloaded and extracted successfully.",
        "upload.commit_fail": "Failed to fetch commit information. Status code: {status}",

        # startup update check
        "startup_update.checking": "Checking for updates...",
        "startup_update.up_to_date": "Up to date version",
        "startup_update.available": "New update available",
        "startup_update.prompt": "Hey, a new update is available! Download the updated version by running the file {file}",
    },

    "it": {
        "app.python_version_error": "Installa una versione di Python > 3.11",
        "app.press_any_key": "Premi un tasto qualsiasi per tornare al menu principale...",
        "error.generic": "Errore: {status}",

        "menu.title": "Menu:",
        "menu.option.download": "Scarica film o serie TV",
        "menu.option.settings": "Impostazioni",
        "menu.option.history": "Cronologia ricerche e download",
        "menu.option.about": "About SCDownloader",
        "menu.choose_option": "Seleziona un'opzione",
        "menu.invalid_option": "Opzione non valida.",

        # history
        "history.title": "Cronologia ricerche e download",
        "history.searches_title": "Ricerche recenti",
        "history.downloads_title": "Download recenti",
        "history.empty": "Non ci sono elementi da visualizzare.",
        "table.when.col": "Quando",
        "table.query.col": "Termine cercato",

        "download.init": "Inizializzazione:",
        "download.search.title": "Ricerca",
        "download.search.prompt": "Inserisci una parola da cercare nel sito",
        "download.search.empty": "Nessun elemento trovato.",
        "download.search.help1": "Inserisci il [value]numero[/] indice, [value][1-2][/] per un intervallo, [value][1,3,5][/] per titoli non consecutivi.",
        "download.search.help2": "Per le serie TV potrai scegliere anche stagione ed episodio da scaricare.",
        "download.index_prompt": "Indice da scaricare",
        "download.movie_selected": "Film selezionato:",
        "download.tv_selected": "Serie TV selezionata:",
        "download.completed": "Coda download completata.",
        "download.summary_title": "Riepilogo download",
        "download.status.success": "Scaricato",
        "download.status.failed": "Non scaricato",
        "download.retry_prompt": "Vuoi riprovare a scaricare i titoli andati in errore?",

        "settings.title": "Impostazioni",
        "settings.menu.domain": "Dominio",
        "settings.menu.language": "Lingua",
        "settings.menu.back": "Torna al menu principale",
        "settings.language.current": "Lingua attuale",
        "settings.language.prompt": "Scegli una lingua",
        "settings.language.saved": "Lingua salvata",

        "about.title": "About SCDownloader",
        "about.text1": "[info]SCDownloader e' stato creato da[/] [value]BarbieGirl♥[/] [info]nel 2026, per puro scopo didattico.[/]",
        "about.text2": "[info]Non ha fini di lucro e puo' essere scaricato, modificato e utilizzato da chiunque.[/]",
        "about.text3": "[warning]Chi lo utilizza per scaricare materiale protetto da copyright o comunque illegale se ne assume la piena responsabilita'.[/]",

        "domain.prompt": "Inserisci il dominio completo (es. streamingcommunity.report): ",
        "domain.empty": "Dominio vuoto, riprova.",
        "domain.testing": "Test dominio:",
        "domain.working": "Dominio funzionante:",
        "domain.invalid": "Il dominio inserito non risponde, non esiste o non e' scritto bene. Reinseriscilo.",
        "domain.loading_rules": "Recupero regole in corso...",
        "domain.not_configured": "Nessun dominio configurato. Vai su [value]Impostazioni[/] per configurarlo.",
        "domain.saved_broken": "[error]Il dominio salvato[/] [value]{domain}[/] [error]non risponde piu'. Vai su[/] [value]Impostazioni[/] [error]per aggiornarlo.[/]",
        "domain.current_saved": "Dominio attualmente salvato:",
        "domain.change_prompt": "Vuoi cambiarlo?",
        "domain.confirmed": "Dominio confermato:",
        "domain.saved": "Dominio salvato:",

        "table.title.col": "Titolo",
        "table.year.col": "Anno",
        "table.type.col": "Tipo",
        "table.episode.col": "Ep.",
        "type.movie": "Film",
        "type.tv": "Serie TV",
        "common.yes": "si",

        "tv.no_valid_video": "Impossibile trovare una qualita' video valida nella playlist",
        "tv.download_episode": "Download episodio:",
        "tv.audio_track_used": "Uso traccia audio m3u8:",
        "tv.seasons_found": "Stagioni trovate:",
        "tv.season_help": "Inserisci il [value]numero[/] della stagione, [value](*)[/] per tutte le stagioni, [value][1-2][/] per un intervallo.",
        "tv.season_prompt": "Numero stagione",
        "tv.episode_help": "Inserisci il [value]numero[/] dell'episodio, [value](*)[/] per tutti gli episodi, [value][1-2][/] per un intervallo.",
        "tv.episode_prompt": "Numero episodio",

        "film.unavailable": "Impossibile riprodurre questo video (non disponibile)",

        "m3u8.parse_error": "Errore nel parsing del contenuto M3U8: {error}",
        "m3u8.no_video_playlist": "Nessuna playlist video trovata",
        "m3u8.download_subtitle": "Download sottotitolo:",
        "m3u8.no_subtitle": "Nessun sottotitolo trovato",
        "m3u8.found_audio_playlists": "Trovate {count} playlist con audio",
        "m3u8.no_audio_playlist": "Impossibile trovare playlist con audio",
        "m3u8.invalid": "M3u8 non valido, errore: {status}",
        "m3u8.task_error": "Si e' verificato un errore: {error}",
        "m3u8.retry": "Tentativo {attempt}/{max}: {count} segmenti falliti (attesa {backoff}s)",
        "m3u8.progress.download": "Scaricamento",
        "m3u8.progress.retry": "Tentativo",
        "m3u8.incomplete_title": "ATTENZIONE: download incompleto",
        "m3u8.incomplete_body1": "{failed} segmenti su {total} NON sono stati scaricati dopo {max} tentativi.",
        "m3u8.incomplete_body2": "Il file risultante avra' dei vuoti/salti in corrispondenza di questi punti.",
        "m3u8.no_progress": "Nessun progresso da {seconds} secondi.",
        "m3u8.breaking_pool": "Interruzione ThreadPoolExecutor...",
        "m3u8.joining_files": "Inizio unione di tutti i file",
        "m3u8.save_error": "Errore nel salvataggio del MP4: {error}",
        "m3u8.cleaning": "Pulizia in corso...",
        "m3u8.download_video": "Download segmenti video",
        "m3u8.download_audio": "Download segmenti audio",
        "m3u8.merge_success": "File video creato con successo.",
        "m3u8.sync_mismatch_title": "ATTENZIONE: audio e video non sincronizzati",
        "m3u8.sync_mismatch_body": "La durata del video ({video}) e quella dell'audio ({audio}) non corrispondono a sufficienza — probabilmente provengono da fonti diverse. Download scartato.",
        "m3u8.merge_error": "Errore nell'unione audio/video: {error}",
        "m3u8.merge_kept_raw": "Video e audio grezzi mantenuti in: {video} , {audio}",
        "m3u8.invalid_url": "Url non valido, errore: {status}",
        "m3u8.download_from_playlist": "Download m3u8 dalla playlist",
        "m3u8.language_selected": "Lingua selezionata:",
        "m3u8.index_selected": "Indice m3u8 selezionato:",
        "m3u8.no_valid_index": "Impossibile trovare un indice m3u8 valido",
        "m3u8.download_from_index": "Download m3u8 dall'indice:",

        "ffmpeg.downloading": "Download di FFmpeg in corso...",
        "ffmpeg.checking": "Verifica di ffmpeg in corso...",
        "ffmpeg.found": "Trovato",
        "ffmpeg.not_in_path": "FFmpeg non e' nel PATH. Download e aggiunta al PATH in corso...",
        "ffmpeg.need_admin": "Devi essere amministratore per procedere!",
        "ffmpeg.download_failed": "Impossibile scaricare o aggiungere FFmpeg al PATH.",
        "ffmpeg.missing.title": "FFmpeg e' necessario ma non e' stato trovato sul tuo sistema.",
        "ffmpeg.missing.what": "FFmpeg serve per scaricare e unire i file video/audio: senza, l'app non puo' funzionare.",
        "ffmpeg.missing.macos.brew_about": "Su macOS il modo piu' semplice per installarlo e' tramite Homebrew, il gestore di pacchetti standard per gli strumenti da riga di comando.",
        "ffmpeg.missing.macos.brew_check": "Non sembra che tu abbia ancora Homebrew. Installalo eseguendo questo comando nel Terminale:",
        "ffmpeg.missing.macos.brew_install_ffmpeg": "Poi installa FFmpeg con:",
        "ffmpeg.missing.linux.hint": "Installalo con il gestore di pacchetti della tua distribuzione, ad esempio:",
        "ffmpeg.missing.retry": "Una volta installato, riavvia l'app.",

        "duration.error": "Errore: {error}",
        "duration.label": "Durata",

        "selection.empty_brackets": "Formato non valido: parentesi vuote.",
        "selection.invalid_list": "Formato lista non valido: '{text}'. Usa [N,M,K] con numeri interi, es. [1,3,5].",
        "selection.invalid_range": "Formato intervallo non valido: '{text}'. Usa [N-M], es. [1-2].",
        "selection.invalid_range_numbers": "Formato intervallo non valido: '{text}'. Usa [N-M] con numeri interi, es. [1-2].",
        "selection.out_of_range_list": "Indici fuori range (1-{max}): {list}",
        "selection.invalid_format": "'{text}' non e' un formato valido. Usa un numero, '*' oppure [N-M] (es. [1-2]).",
        "selection.out_of_range": "Indice fuori range: deve essere tra 1 e {max}.",
        "selection.retry_suffix": "Riprova.",
        "selection.cancel_hint": "Inserisci [value]0[/] per tornare indietro.",

        "fs.remove_folder_error": "Errore nella rimozione della cartella '{path}': {error}",
        "fs.remove_file_error": "Errore nella rimozione del file '{path}': {error}",
        "fs.file_not_found": "Il file '{path}' non esiste.",

        "update.checking": "Verifica versione github in corso...",
        "update.new_version": "E' disponibile una nuova versione:",
        "update.version_label": "Versione:",
        "update.up_to_date": "Tutto aggiornato",
        "update.latest_version": "Ultima versione:",
        "update.stats": "{repo} e' stato scaricato {count} volte, ma solo il {percent}% di voi(!!) ha messo una stella.\nAiuta la crescita del repository oggi, lasciando una stella e condividendolo con altri online!",
        "upload.invalid_dir": "Errore: '{dir}' non e' una directory valida.",
        "upload.permission_error": "Errore di permessi: {error}. Controlla i permessi e prova a eseguire lo script come amministratore.",
        "upload.generic_error": "Errore: {error}",
        "upload.requesting_repo": "Richiesta al repository github in corso",
        "upload.fetching_zip": "Recupero del file zip dal repository",
        "upload.extracting": "Estrazione dei file in corso...",
        "upload.commit_success": "Ultimo commit scaricato ed estratto con successo.",
        "upload.commit_fail": "Recupero informazioni sul commit non riuscito. Codice di stato: {status}",

        # controllo aggiornamenti all'avvio
        "startup_update.checking": "Controllo aggiornamenti...",
        "startup_update.up_to_date": "Versione aggiornata",
        "startup_update.available": "Nuovo aggiornamento disponibile",
        "startup_update.prompt": "Ehy, c'e' un nuovo aggiornamento disponibile! Scarica la versione aggiornata lanciando il file {file}",
    },

    "es": {
        "app.python_version_error": "Instala una version de Python > 3.11",
        "app.press_any_key": "Pulsa una tecla para volver al menu principal...",
        "error.generic": "Error: {status}",

        "menu.title": "Menu:",
        "menu.option.download": "Descargar una pelicula o serie de TV",
        "menu.option.settings": "Ajustes",
        "menu.option.history": "Historial de busquedas y descargas",
        "menu.option.about": "Acerca de SCDownloader",
        "menu.choose_option": "Elige una opcion",
        "menu.invalid_option": "Opcion no valida.",

        # history
        "history.title": "Historial de busquedas y descargas",
        "history.searches_title": "Busquedas recientes",
        "history.downloads_title": "Descargas recientes",
        "history.empty": "No hay elementos para mostrar.",
        "table.when.col": "Cuando",
        "table.query.col": "Termino buscado",

        "download.init": "Inicializacion:",
        "download.search.title": "Busqueda",
        "download.search.prompt": "Escribe una palabra para buscar en el sitio",
        "download.search.empty": "No se encontraron resultados.",
        "download.search.help1": "Escribe un numero de [value]indice[/], [value][1-2][/] para un rango, [value][1,3,5][/] para titulos no consecutivos.",
        "download.search.help2": "Para las series de TV tambien podras elegir la temporada y el episodio a descargar.",
        "download.index_prompt": "Indice a descargar",
        "download.movie_selected": "Pelicula seleccionada:",
        "download.tv_selected": "Serie de TV seleccionada:",
        "download.completed": "Cola de descargas completada.",
        "download.summary_title": "Resumen de descargas",
        "download.status.success": "Descargado",
        "download.status.failed": "No descargado",
        "download.retry_prompt": "¿Quieres reintentar descargar los titulos que fallaron?",

        "settings.title": "Ajustes",
        "settings.menu.domain": "Dominio",
        "settings.menu.language": "Idioma",
        "settings.menu.back": "Volver al menu principal",
        "settings.language.current": "Idioma actual",
        "settings.language.prompt": "Elige un idioma",
        "settings.language.saved": "Idioma guardado",

        "about.title": "Acerca de SCDownloader",
        "about.text1": "[info]SCDownloader fue creado por[/] [value]BarbieGirl♥[/] [info]en 2026, con fines puramente educativos.[/]",
        "about.text2": "[info]No tiene fines de lucro y puede ser descargado, modificado y utilizado por cualquiera.[/]",
        "about.text3": "[warning]Quien lo utilice para descargar material protegido por derechos de autor o ilegal asume toda la responsabilidad.[/]",

        "domain.prompt": "Introduce el dominio completo (ej. streamingcommunity.report): ",
        "domain.empty": "Dominio vacio, intentalo de nuevo.",
        "domain.testing": "Probando dominio:",
        "domain.working": "Dominio funcionando:",
        "domain.invalid": "El dominio introducido no responde, no existe o no esta bien escrito. Vuelve a intentarlo.",
        "domain.loading_rules": "Obteniendo reglas...",
        "domain.not_configured": "No hay ningun dominio configurado. Ve a [value]Ajustes[/] para configurarlo.",
        "domain.saved_broken": "[error]El dominio guardado[/] [value]{domain}[/] [error]ya no responde. Ve a[/] [value]Ajustes[/] [error]para actualizarlo.[/]",
        "domain.current_saved": "Dominio guardado actualmente:",
        "domain.change_prompt": "¿Quieres cambiarlo?",
        "domain.confirmed": "Dominio confirmado:",
        "domain.saved": "Dominio guardado:",

        "table.title.col": "Titulo",
        "table.year.col": "Año",
        "table.type.col": "Tipo",
        "table.episode.col": "Ep.",
        "type.movie": "Pelicula",
        "type.tv": "Serie de TV",
        "common.yes": "si",

        "tv.no_valid_video": "No se pudo encontrar una calidad de video valida en la playlist",
        "tv.download_episode": "Descargando episodio:",
        "tv.audio_track_used": "Usando pista de audio m3u8:",
        "tv.seasons_found": "Temporadas encontradas:",
        "tv.season_help": "Escribe el [value]numero[/] de la temporada, [value](*)[/] para todas las temporadas, [value][1-2][/] para un rango.",
        "tv.season_prompt": "Numero de temporada",
        "tv.episode_help": "Escribe el [value]numero[/] del episodio, [value](*)[/] para todos los episodios, [value][1-2][/] para un rango.",
        "tv.episode_prompt": "Numero de episodio",

        "film.unavailable": "No se puede reproducir este video (no disponible)",

        "m3u8.parse_error": "Error al analizar el contenido M3U8: {error}",
        "m3u8.no_video_playlist": "No se encontro ninguna playlist de video",
        "m3u8.download_subtitle": "Descargando subtitulo:",
        "m3u8.no_subtitle": "No se encontro ningun subtitulo",
        "m3u8.found_audio_playlists": "Se encontraron {count} playlists con audio",
        "m3u8.no_audio_playlist": "No se pudo encontrar una playlist con audio",
        "m3u8.invalid": "M3u8 no valido, error: {status}",
        "m3u8.task_error": "Se produjo un error: {error}",
        "m3u8.retry": "Intento {attempt}/{max}: {count} segmentos fallidos (esperando {backoff}s)",
        "m3u8.progress.download": "Descargando",
        "m3u8.progress.retry": "Reintentando",
        "m3u8.incomplete_title": "ATENCION: descarga incompleta",
        "m3u8.incomplete_body1": "{failed} de {total} segmentos NO se descargaron tras {max} intentos.",
        "m3u8.incomplete_body2": "El archivo resultante tendra huecos/saltos en esos puntos.",
        "m3u8.no_progress": "Sin progreso durante {seconds} segundos.",
        "m3u8.breaking_pool": "Deteniendo el ThreadPoolExecutor...",
        "m3u8.joining_files": "Uniendo todos los archivos",
        "m3u8.save_error": "Error al guardar el MP4: {error}",
        "m3u8.cleaning": "Limpiando...",
        "m3u8.download_video": "Descargando segmentos de video",
        "m3u8.download_audio": "Descargando segmentos de audio",
        "m3u8.merge_success": "Archivo de video creado con exito.",
        "m3u8.sync_mismatch_title": "ATENCION: audio y video desincronizados",
        "m3u8.sync_mismatch_body": "La duracion del video ({video}) y la del audio ({audio}) no coinciden lo suficiente — probablemente provienen de fuentes distintas. Descartando esta descarga.",
        "m3u8.merge_error": "Error al unir audio/video: {error}",
        "m3u8.merge_kept_raw": "Video y audio en bruto conservados en: {video} , {audio}",
        "m3u8.invalid_url": "URL no valida, error: {status}",
        "m3u8.download_from_playlist": "Descargando m3u8 desde la playlist",
        "m3u8.language_selected": "Idioma seleccionado:",
        "m3u8.index_selected": "Indice m3u8 seleccionado:",
        "m3u8.no_valid_index": "No se pudo encontrar un indice m3u8 valido",
        "m3u8.download_from_index": "Descargando m3u8 desde el indice:",

        "ffmpeg.downloading": "Descargando FFmpeg...",
        "ffmpeg.checking": "Comprobando ffmpeg...",
        "ffmpeg.found": "Encontrado",
        "ffmpeg.not_in_path": "FFmpeg no esta en el PATH. Descargando y añadiendolo al PATH...",
        "ffmpeg.need_admin": "¡Necesitas ser administrador para continuar!",
        "ffmpeg.download_failed": "No se pudo descargar o añadir FFmpeg al PATH.",
        "ffmpeg.missing.title": "Se necesita FFmpeg pero no se encontro en tu sistema.",
        "ffmpeg.missing.what": "FFmpeg se usa para descargar y unir los archivos de video/audio: sin el, la app no puede funcionar.",
        "ffmpeg.missing.macos.brew_about": "En macOS la forma mas facil de instalarlo es con Homebrew, el gestor de paquetes estandar para herramientas de linea de comandos.",
        "ffmpeg.missing.macos.brew_check": "Parece que aun no tienes Homebrew. Instalalo ejecutando este comando en Terminal:",
        "ffmpeg.missing.macos.brew_install_ffmpeg": "Luego instala FFmpeg con:",
        "ffmpeg.missing.linux.hint": "Instalalo con el gestor de paquetes de tu distribucion, por ejemplo:",
        "ffmpeg.missing.retry": "Una vez instalado, vuelve a ejecutar la app.",

        "duration.error": "Error: {error}",
        "duration.label": "Duracion",

        "selection.empty_brackets": "Formato no valido: corchetes vacios.",
        "selection.invalid_list": "Formato de lista no valido: '{text}'. Usa [N,M,K] con numeros enteros, ej. [1,3,5].",
        "selection.invalid_range": "Formato de rango no valido: '{text}'. Usa [N-M], ej. [1-2].",
        "selection.invalid_range_numbers": "Formato de rango no valido: '{text}'. Usa [N-M] con numeros enteros, ej. [1-2].",
        "selection.out_of_range_list": "Indices fuera de rango (1-{max}): {list}",
        "selection.invalid_format": "'{text}' no es un formato valido. Usa un numero, '*' o [N-M] (ej. [1-2]).",
        "selection.out_of_range": "Indice fuera de rango: debe estar entre 1 y {max}.",
        "selection.retry_suffix": "Intentalo de nuevo.",
        "selection.cancel_hint": "Escribe [value]0[/] para volver atras.",

        "fs.remove_folder_error": "Error al eliminar la carpeta '{path}': {error}",
        "fs.remove_file_error": "Error al eliminar el archivo '{path}': {error}",
        "fs.file_not_found": "El archivo '{path}' no existe.",

        "update.checking": "Comprobando version de github...",
        "update.new_version": "Hay una nueva version disponible:",
        "update.version_label": "Version:",
        "update.up_to_date": "Todo esta actualizado",
        "update.latest_version": "Ultima version:",
        "update.stats": "{repo} se ha descargado {count} veces, pero solo el {percent}% de vosotros(!!) le ha dado una estrella.\n¡Ayuda a que crezca el repositorio hoy, dejando una estrella y compartiendolo online!",
        "upload.invalid_dir": "Error: '{dir}' no es un directorio valido.",
        "upload.permission_error": "Error de permisos: {error}. Comprueba los permisos e intenta ejecutar el script como administrador.",
        "upload.generic_error": "Error: {error}",
        "upload.requesting_repo": "Solicitando el repositorio de github",
        "upload.fetching_zip": "Obteniendo el archivo zip del repositorio",
        "upload.extracting": "Extrayendo archivos...",
        "upload.commit_success": "Ultimo commit descargado y extraido con exito.",
        "upload.commit_fail": "No se pudo obtener la informacion del commit. Codigo de estado: {status}",

        # comprobacion de actualizaciones al inicio
        "startup_update.checking": "Comprobando actualizaciones...",
        "startup_update.up_to_date": "Version actualizada",
        "startup_update.available": "Nueva actualizacion disponible",
        "startup_update.prompt": "¡Oye, hay una nueva actualizacion disponible! Descarga la version actualizada ejecutando el archivo {file}",
    },
}


def t(key, **kwargs):
    """Return the translated string for `key` in the current language, formatted with kwargs."""

    template = TRANSLATIONS.get(_current_language, {}).get(key)
    if template is None:
        template = TRANSLATIONS[DEFAULT_LANGUAGE].get(key, key)

    return template.format(**kwargs) if kwargs else template


def get_language():
    return _current_language


def set_language(lang_code):
    """Change the current language and persist it to data.json."""

    global _current_language
    if lang_code not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {lang_code}")

    _current_language = lang_code

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data['language'] = lang_code
    with open('data.json', 'w') as file:
        json.dump(data, file)


def load_language():
    """Load the saved language preference (if any) from data.json. Falls back to the default."""

    global _current_language

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    lang_code = data.get('language')
    _current_language = lang_code if lang_code in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE
