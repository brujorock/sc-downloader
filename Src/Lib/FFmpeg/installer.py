# 24.01.2023

# Class
from Src.Util.console import console
from Src.Util.i18n import t

# Import
import subprocess, os, requests, zipfile, sys, ctypes, platform

# Variable
HOMEBREW_INSTALL_CMD = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'


# [ func ]
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def download_ffmpeg():
    """Windows only: fetch a prebuilt FFmpeg and add it to PATH for this run."""

    # Specify the URL for the FFmpeg binary zip file for Windows
    ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z"

    # Name of the directory where FFmpeg will be extracted
    ffmpeg_dir = "ffmpeg"
    console.print(f"[warning]{t('ffmpeg.downloading')}[/]")

    # Download the FFmpeg zip file
    response = requests.get(ffmpeg_url)
    os.makedirs(ffmpeg_dir, exist_ok=True)

    # Save the zip file
    zip_file_path = os.path.join(ffmpeg_dir, "ffmpeg.zip")
    with open(zip_file_path, "wb") as zip_file:
        zip_file.write(response.content)

    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(ffmpeg_dir)

    # Add the FFmpeg directory to the system PATH
    ffmpeg_bin_dir = os.path.join(os.getcwd(), ffmpeg_dir, "bin")
    os.environ["PATH"] += os.pathsep + ffmpeg_bin_dir
    os.remove(zip_file_path)

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

def check_ffmpeg():

    console.print(f"[info]{t('ffmpeg.checking')}[/]", end="")

    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        console.print(f" [success]✓ {t('ffmpeg.found')}[/]")
        return
    except Exception:
        console.print()

    system = platform.system()

    if system == "Darwin":
        show_macos_instructions()
        sys.exit(0)

    if system == "Linux":
        show_linux_instructions()
        sys.exit(0)

    # Windows: keep the existing auto-download behavior
    try:
        console.print(f"[warning]{t('ffmpeg.not_in_path')}[/]")

        if not isAdmin():
            console.log(f"[error]{t('ffmpeg.need_admin')}[/]")
            sys.exit(0)

        download_ffmpeg()
        sys.exit(0)
    except Exception:
        console.print(f"[error]{t('ffmpeg.download_failed')}[/]")
        sys.exit(0)
