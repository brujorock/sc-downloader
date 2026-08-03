# 3.12.23 -> 10.12.23

# Class import
from Src.Util.headers import get_headers
from Src.Util.console import console
from Src.Util.selection import ask_selection
from Src.Util.i18n import t
from Src.Lib.FFmpeg.my_m3u8 import download_m3u8

# General import
import requests, os, re, sys
from bs4 import BeautifulSoup
from rich.table import Table
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode


# [func]
def get_token(id_tv, domain):
    session = requests.Session()
    session.get(f"https://{domain}/it/watch/{id_tv}")
    return session.cookies['XSRF-TOKEN']

def get_info_tv(id_film, title_name, site_version, domain):

    req = requests.get(f"https://{domain}/it/titles/{id_film}-{title_name}", headers={
        'X-Inertia': 'true',
        'X-Inertia-Version': site_version,
        'User-Agent': get_headers()
    })

    if req.ok:
        return req.json()['props']['title']['seasons_count']
    else:
        console.log(f"[error]{t('error.generic', status=req.status_code)}[/]")
        sys.exit(0)

def get_info_season(tv_id, tv_name, domain, version, token, n_stagione):
    req = requests.get(f'https://{domain}/it/titles/{tv_id}-{tv_name}/season-{n_stagione}', headers={
        'authority': domain, 'referer': f'https://{domain}/it/titles/{tv_id}-{tv_name}',
        'user-agent': get_headers(), 'x-inertia': 'true', 'x-inertia-version': version, 'x-xsrf-token': token,
    })

    if req.ok:
        return [{'id': ep['id'], 'n': ep['number'], 'name': ep['name']} for ep in req.json()['props']['loadedSeason']['episodes']]
    else:
        console.log(f"[error]{t('error.generic', status=req.status_code)}[/]")
        sys.exit(0)

def get_iframe(tv_id, ep_id, domain, token):
    req = requests.get(f'https://{domain}/it/iframe/{tv_id}', params={'episode_id': ep_id, 'next_episode': '1'}, cookies={'XSRF-TOKEN': token}, headers={
        'referer': f'https://{domain}/it/watch/{tv_id}?e={ep_id}',
        'user-agent': get_headers()
    })

    if req.ok:
        url_embed = BeautifulSoup(req.text, "lxml").find("iframe").get("src")
        req_embed = requests.get(url_embed, headers = {"User-agent": get_headers()}).text
        embed_script = BeautifulSoup(req_embed, "lxml").find("body").find("script").text
        return embed_script, url_embed
    else:
        console.log(f"[error]{t('error.generic', status=req.status_code)}[/]")
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
        console.log(f"[error]{t('error.generic', status=req.status_code)}[/]")
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
        console.log(f"[error]{t('tv.no_valid_video')}[/]")
        sys.exit(0)

    video_url = max(video_candidates, key=lambda x: x[0])[1]
    audio_url = next((uri for is_ita, uri in audio_candidates if is_ita), audio_candidates[0][1] if audio_candidates else None)

    return video_url, audio_url

def get_m3u8_key(url_embed):
    req = requests.get('https://vixcloud.co/storage/enc.key', headers={'referer': url_embed, 'user-agent': get_headers()})

    if req.ok:
        return "".join(["{:02x}".format(c) for c in req.content])
    else:
        console.log(f"[error]{t('error.generic', status=req.status_code)}[/]")
        sys.exit(0)


# [func \ main]
def dw_single_ep(tv_id, eps, index_ep_select, domain, token, tv_name, season_select):

    console.print(f"[title]{t('tv.download_episode')}[/] [value]{eps[index_ep_select]['n']} - {eps[index_ep_select]['name']}[/]")
    embed_script, url_embed = get_iframe(tv_id, eps[index_ep_select]['id'], domain, token)
    m3u8_playlist = get_master_playlist(embed_script, url_embed)
    m3u8_url, m3u8_url_audio = select_video_audio(m3u8_playlist)
    m3u8_key = get_m3u8_key(url_embed)

    mp4_name = f"{tv_name.replace('+', '_')}_S{str(season_select).zfill(2)}E{str(index_ep_select+1).zfill(2)}"
    mp4_format = f"{mp4_name}.mp4"
    mp4_path = os.path.join("downloads", "tv", tv_name, mp4_format)

    if m3u8_url_audio != None:
        console.print(f"[info]{t('tv.audio_track_used')}[/] [success]{t('common.yes')}[/]")

    download_m3u8(m3u8_index=m3u8_url, m3u8_audio=m3u8_url_audio, m3u8_subtitle=m3u8_playlist, key=m3u8_key, output_filename=mp4_path, subtitle_prefix=mp4_name)

def main_dw_tv(tv_id, tv_name, version, domain):

    token = get_token(tv_id, domain)

    num_season_find = get_info_tv(tv_id, tv_name, version, domain)
    console.print(f"[info]{t('tv.seasons_found')}[/] [value]{num_season_find}[/]")
    console.print(f"[info]{t('tv.season_help')}[/]")
    seasons_to_download = ask_selection(f"[prompt]{t('tv.season_prompt')}[/]", num_season_find)

    for season_select in seasons_to_download:
        eps = get_info_season(tv_id, tv_name, domain, version, token, season_select)

        if len(seasons_to_download) == 1:
            # A single season was picked: let the user choose which episodes.
            console.print()
            table = Table(show_header=True, header_style="title", border_style="muted")
            table.add_column(t("table.episode.col"), style="accent", justify="right")
            table.add_column(t("table.title.col"), style="value")
            for ep in eps:
                table.add_row(str(ep['n']), ep['name'])
            console.print(table)

            console.print(f"[info]{t('tv.episode_help')}[/]")
            eps_to_download = ask_selection(f"[prompt]{t('tv.episode_prompt')}[/]", len(eps))
        else:
            # Multiple/all seasons were picked: download every episode of each.
            eps_to_download = list(range(1, len(eps) + 1))

        for ep_index in eps_to_download:
            console.print()
            console.rule(style="muted")
            dw_single_ep(tv_id, eps, ep_index - 1, domain, token, tv_name, season_select)

