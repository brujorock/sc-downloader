# 3.12.23 -> 10.12.23

# Class import
from Src.Util.headers import get_headers
from Src.Util.console import console
from Src.Lib.FFmpeg.my_m3u8 import download_m3u8

# General import
import requests, os, re, sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode

# [func]
def get_iframe(id_title, title_slug, domain):
    # Visit the title page first (like a real browser navigating there) so we
    # carry a real session/cookies into the iframe request instead of firing
    # it cold, which sites are more likely to flag and block with a 403.
    session = requests.Session()
    title_url = f"https://{domain}/it/titles/{id_title}-{title_slug}"
    session.get(title_url, headers={"user-agent": get_headers()})

    req = session.get(url = f"https://{domain}/it/iframe/{id_title}", headers = {
        "user-agent": get_headers(),
        "referer": title_url
    })

    if req.ok:
        url_embed = BeautifulSoup(req.text, "lxml").find("iframe").get("src")
        req_embed = session.get(url_embed, headers = {"user-agent": get_headers(), "referer": title_url}).text

        try:
            embed_script = BeautifulSoup(req_embed, "lxml").find("body").find("script").text
            return embed_script, url_embed
        except:
            console.log("[error]Impossibile riprodurre questo video (non disponibile)[/]")
            sys.exit(0)

    else:
        console.log(f"[error]Errore: {req.status_code}[/]")
        sys.exit(0)

def get_master_playlist_url(embed_script, url_embed):
    """Rebuild the master playlist url the same way the player js does (masterPlaylist.url + params + h/scz/lang)"""

    playlist_base = re.search(r"url:\s*'([^']+)'", embed_script).group(1)
    token = re.search(r"'token':\s*'([^']+)'", embed_script).group(1)
    expires = re.search(r"'expires':\s*'([^']+)'", embed_script).group(1)

    embed_params = dict(parse_qsl(urlparse(url_embed).query))
    params = {'token': token, 'expires': expires}
    if embed_params.get('canPlayFHD'):
        params['h'] = 1
    if embed_params.get('scz'):
        params['scz'] = 1
    params['lang'] = embed_params.get('lang', 'en')

    # playlist_base can already carry its own query string (e.g. "?b=1" on some
    # titles); merge instead of blindly concatenating or we end up with an
    # invalid "...?b=1?token=..." URL that gets rejected with a 403.
    parsed_base = urlparse(playlist_base)
    merged_params = dict(parse_qsl(parsed_base.query))
    merged_params.update(params)

    return urlunparse(parsed_base._replace(query=urlencode(merged_params)))

def get_master_playlist(embed_script, url_embed):
    playlist_url = get_master_playlist_url(embed_script, url_embed)
    req = requests.get(playlist_url, headers={'referer': url_embed, 'user-agent': get_headers()})

    if req.ok:
        return req.text
    else:
        console.log(f"[error]Errore: {req.status_code}[/]")
        sys.exit(0)

def select_video_audio(m3u8_playlist):
    """Pick the highest bandwidth video rendition and the Italian (or default) audio track"""

    lines = m3u8_playlist.splitlines()
    audio_candidates = []
    video_candidates = []

    for i, line in enumerate(lines):
        if line.startswith("#EXT-X-MEDIA:TYPE=AUDIO"):
            uri_match = re.search(r'URI="([^"]+)"', line)
            if uri_match:
                audio_candidates.append(('LANGUAGE="ita"' in line, uri_match.group(1)))

        elif line.startswith("#EXT-X-STREAM-INF"):
            bandwidth_match = re.search(r"BANDWIDTH=(\d+)", line)
            uri = lines[i + 1] if i + 1 < len(lines) else None
            if uri:
                video_candidates.append((int(bandwidth_match.group(1)) if bandwidth_match else 0, uri))

    if not video_candidates:
        console.log("[error]Impossibile trovare una qualita' video valida nella playlist[/]")
        sys.exit(0)

    video_url = max(video_candidates, key=lambda x: x[0])[1]
    audio_url = next((uri for is_ita, uri in audio_candidates if is_ita), audio_candidates[0][1] if audio_candidates else None)

    return video_url, audio_url

def get_m3u8_key(url_embed):
    req = requests.get('https://vixcloud.co/storage/enc.key', headers={'referer': url_embed, 'user-agent': get_headers()})

    if req.ok:
        return "".join(["{:02x}".format(c) for c in req.content])
    else:
        console.log(f"[error]Errore: {req.status_code}[/]")
        sys.exit(0)


# [func \ main]
def main_dw_film(id_film, title_name, domain):

    embed_script, url_embed = get_iframe(id_film, title_name, domain)
    m3u8_playlist = get_master_playlist(embed_script, url_embed)
    m3u8_url, m3u8_url_audio = select_video_audio(m3u8_playlist)
    m3u8_key = get_m3u8_key(url_embed)

    mp4_name = title_name.replace("+", " ").replace(",", "")
    mp4_format = mp4_name + ".mp4"
    mp4_path = os.path.join("downloads", "film", mp4_name, mp4_format)

    if m3u8_url_audio != None:
        console.print("[info]Uso traccia audio m3u8:[/] [success]si[/]")

    download_m3u8(m3u8_index=m3u8_url, m3u8_audio=m3u8_url_audio, m3u8_subtitle=m3u8_playlist, key=m3u8_key, output_filename=mp4_path)
