# 31.01.24

# Class
from Src.Util.console import console
from Src.Util.i18n import t

# Import
import ffmpeg

# Variable
SYNC_TOLERANCE_SECONDS = 3  # max allowed gap between video/audio duration before treating them as mismatched


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
    """Print the file's duration and also return it (in seconds, or None if it couldn't be read)."""

    video_duration = get_video_duration(file_path)

    if video_duration is not None:
        hours, minutes, seconds = format_duration(video_duration)
        console.log(f"[muted]{t('duration.label')}[/] [value]'{file_path}'[/]: [accent]{int(hours)}h {int(minutes)}m {int(seconds)}s[/]")

    return video_duration

def durations_compatible(duration_a, duration_b, tolerance=SYNC_TOLERANCE_SECONDS):
    """Whether two durations are close enough to belong to the same video/audio pair.

    Unknown durations (None, when ffprobe couldn't read a file) are treated as
    incompatible rather than optimistically skipped, since we can't verify them.
    """

    if duration_a is None or duration_b is None:
        return False

    return abs(duration_a - duration_b) <= tolerance
