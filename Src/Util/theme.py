# Central place for the app's color scheme / visual style.
#
# To change the look of the whole app, edit the colors below — nothing else
# needs to change. Every console message in the project uses these semantic
# names (e.g. "[success]...[/]") instead of raw colors, so the meaning of a
# message (success, error, a value, ...) always maps to the same color.
#
# Current palette: "Barbie" theme, colors taken from:
#   https://github.com/mihtoa/barbie-theme (themes/barbie-theme-color-theme.json)
#   https://marketplace.visualstudio.com/items?itemName=mo0on.barbie-dark-theme

from rich.theme import Theme

THEME = Theme({
    # Brand / structural
    "brand": "bold #F11EA6",            # ASCII logo — signature Barbie hot pink
    "title": "bold #CF1A7F",            # section headers / rules — deep pink
    "muted": "dim #FFCEF0",             # secondary, low-importance text — dusty pale pink

    # Feedback
    "success": "bold #0DBC79",
    "error": "bold #F14C4C",
    "warning": "bold #E5C110",
    "info": "bold #D670D6",             # bright magenta

    # Interactive
    "prompt": "bold #F11EA6",           # questions asked to the user
    "value": "bold #FFCEF0",            # dynamic values: domain, titles, numbers, paths
    "accent": "bold #BC3FBC",           # list indexes / bullets
})
