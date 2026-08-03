# 31.01.24

# Class
from Src.Util.console import console
from Src.Util.i18n import t

# Import
import ffmpeg

# Variable


# [ func ]
def get_video_duration(file_path):
    try:
        probe = ffmpeg.probe(file_path)
        duration = float(probe['format']['duration'])
        return duration
    except ffmpeg.Error as e:
        print(t("duration.error", error=e.stderr))
        return None

def format_duration(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)

def print_duration_table(file_path):
    video_duration = get_video_duration(file_path)

    if video_duration is not None:
        hours, minutes, seconds = format_duration(video_duration)
        console.log(f"[muted]{t('duration.label')}[/] [value]'{file_path}'[/]: [accent]{int(hours)}h {int(minutes)}m {int(seconds)}s[/]")
