# 3.12.23

# Import
from Src.Util.console import console
from Src.Upload.__version__ import __version__

def msg_start():

    logo = r"""
  _____   _____   _____      __
 / ____| / ____| |  __ \    |  |
| (___   | |     | |  | |   |  |
 \___ \  | |     | |  | |   |  |
 ____) | | |___  | |__| |   \  /
|_____/  \_____| |_____/     \/
"""

    console.print(logo, style="brand", justify="center")
    console.print(f"SCDownloader by BarbieGirl♥ - V {__version__}", style="muted", justify="center")
    console.print()