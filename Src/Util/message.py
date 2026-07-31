# 3.12.23

# Import
from Src.Util.console import console

def msg_start():

    logo = r"""
  _____ _____   _____      __
 / ____|  __ \ / ____|    |  |
| (___ | |  | | |         |  |
 \___ \| |  | | |         |  |
 ____) | |__| | |____     \  /
|_____/|_____/ \_____|     \/
"""

    console.print(logo, style="brand", justify="center")
    console.print("Streaming Community Downloader by BarbieGirl♥", style="muted", justify="center")
    console.print()