# 3.12.23

# Import
from Src.Util.console import console

def msg_start():

    logo = r"""
  _____  _____ _____
 / ____|/ ____|  __ \
| (___ | |    | |  | |
 \___ \| |    | |  | |
 ____) | |____| |__| |
|_____/ \_____|_____/
"""

    console.print(f"[brand]{logo}[/]")
    console.print("[muted]Streaming Community Downloader[/]", justify="center")
    console.print()