# 24.01.2023

# Class
from Src.Util.console import console
from Src.Util.i18n import t

# Import
import subprocess, sys, platform

# Variable
HOMEBREW_INSTALL_CMD = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'


# [ func ]
def has_brew():
    try:
        subprocess.run(["brew", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except Exception:
        return False

def show_macos_instructions():
    console.print(f"[error]{t('ffmpeg.missing.title')}[/]")
    console.print(f"[muted]{t('ffmpeg.missing.what')}[/]")
    console.print()

    if not has_brew():
        console.print(f"[info]{t('ffmpeg.missing.macos.brew_about')}[/]")
        console.print(f"[info]{t('ffmpeg.missing.macos.brew_check')}[/]")
        console.print(f"[value]{HOMEBREW_INSTALL_CMD}[/]")
        console.print()

    console.print(f"[info]{t('ffmpeg.missing.macos.brew_install_ffmpeg')}[/]")
    console.print("[value]brew install ffmpeg[/]")
    console.print()
    console.print(f"[muted]{t('ffmpeg.missing.retry')}[/]")

def show_linux_instructions():
    console.print(f"[error]{t('ffmpeg.missing.title')}[/]")
    console.print(f"[muted]{t('ffmpeg.missing.what')}[/]")
    console.print()
    console.print(f"[info]{t('ffmpeg.missing.linux.hint')}[/]")
    console.print("[value]sudo apt install ffmpeg[/]   [muted](Debian/Ubuntu)[/]")
    console.print("[value]sudo dnf install ffmpeg[/]   [muted](Fedora)[/]")
    console.print("[value]sudo pacman -S ffmpeg[/]   [muted](Arch)[/]")
    console.print()
    console.print(f"[muted]{t('ffmpeg.missing.retry')}[/]")

def has_winget():
    try:
        subprocess.run(["winget", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except Exception:
        return False

def show_windows_instructions():
    console.print(f"[error]{t('ffmpeg.missing.title')}[/]")
    console.print(f"[muted]{t('ffmpeg.missing.what')}[/]")
    console.print()

    if has_winget():
        console.print(f"[info]{t('ffmpeg.missing.windows.winget_hint')}[/]")
        console.print("[value]winget install -e --id Gyan.FFmpeg[/]")
        console.print()

    console.print(f"[info]{t('ffmpeg.missing.windows.manual_hint')}[/]")
    console.print("[value]https://www.gyan.dev/ffmpeg/builds/[/]")
    console.print(f"[muted]{t('ffmpeg.missing.windows.manual_steps')}[/]")
    console.print()
    console.print(f"[muted]{t('ffmpeg.missing.retry')}[/]")

def check_ffmpeg():

    console.print(f"[muted]{t('ffmpeg.checking')}[/]", end="")

    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        console.print(f" [success]✓ {t('ffmpeg.found')}[/]")
        return
    except Exception:
        console.print()

    system = platform.system()

    if system == "Darwin":
        show_macos_instructions()
    elif system == "Linux":
        show_linux_instructions()
    else:
        show_windows_instructions()

    sys.exit(0)
