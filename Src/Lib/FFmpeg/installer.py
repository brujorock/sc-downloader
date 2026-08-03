# 24.01.2023

# Class
from Src.Util.console import console
from Src.Util.i18n import t

# Import
import subprocess, os, requests, zipfile, sys, ctypes, os, sys

# Variable


# [ func ]
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def download_ffmpeg():

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

def check_ffmpeg():

    console.print(f"[info]{t('ffmpeg.checking')}[/]", end="")

    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        console.print(f" [success]✓ {t('ffmpeg.found')}[/]")
    except:
        console.print()
        try:
            console.print(f"[warning]{t('ffmpeg.not_in_path')}[/]")

            if not isAdmin():
                console.log(f"[error]{t('ffmpeg.need_admin')}[/]")
                sys.exit(0)

            download_ffmpeg()
            sys.exit(0)
        except:
            console.print(f"[error]{t('ffmpeg.download_failed')}[/]")
            sys.exit(0)
