# Central place for the app's color scheme / visual style.
#
# To change the look of the whole app, edit the colors below — nothing else
# needs to change. Every console message in the project uses these semantic
# names (e.g. "[success]...[/]") instead of raw colors, so the meaning of a
# message (success, error, a value, ...) always maps to the same color.

from rich.theme import Theme

THEME = Theme({
    # Brand / structural
    "brand": "bold bright_magenta",     # ASCII logo
    "title": "bold cyan",               # section headers / rules
    "muted": "grey62",                  # secondary, low-importance text

    # Feedback
    "success": "bold green",
    "error": "bold red",
    "warning": "bold yellow",
    "info": "cyan",

    # Interactive
    "prompt": "bold cyan",              # questions asked to the user
    "value": "bold white",              # dynamic values: domain, titles, numbers, paths
    "accent": "bold magenta",           # list indexes / bullets
})
