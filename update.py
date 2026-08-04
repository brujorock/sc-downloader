# 10.12.24

# General imports
import requests, os, shutil
from zipfile import ZipFile
from io import BytesIO
from rich.console import Console
from Src.Util.theme import THEME
from Src.Util.i18n import t, load_language
from Src.Upload.update import get_install_version, get_remote_version

# Variable
load_language()
console = Console(theme=THEME)
local_path = os.path.join(".")

def move_content(source, destination):
    
    os.makedirs(destination, exist_ok=True)

    # Iterate through all elements in the source folder
    for element in os.listdir(source):
        source_path = os.path.join(source, element)
        destination_path = os.path.join(destination, element)

        # If it's a directory, recursively call the function
        if os.path.isdir(source_path):
            move_content(source_path, destination_path)
        else:
            # Otherwise, move the file, replacing if it already exists
            shutil.move(source_path, destination_path)

def keep_specific_items(directory, keep_folders, keep_files):
    try:
        if not os.path.exists(directory) or not os.path.isdir(directory):
            raise ValueError(t("upload.invalid_dir", dir=directory))

        # Iterate through items in the directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            # Check if the item is one of the specified folders or files
            if os.path.isdir(item_path) and item not in keep_folders:
                shutil.rmtree(item_path)
            elif os.path.isfile(item_path) and item not in keep_files:
                os.remove(item_path)

    except PermissionError as pe:
        print(t("upload.permission_error", error=pe))
    except Exception as e:
        print(t("upload.generic_error", error=e))

def download_and_extract_latest_commit(author, repo_name):

    # Get the latest commit information using GitHub API
    api_url = f'https://api.github.com/repos/{author}/{repo_name}/commits?per_page=1'
    response = requests.get(api_url)
    console.log(f"[info]{t('upload.requesting_repo')}[/]")

    if response.status_code == 200:
        commit_info = response.json()[0]
        commit_sha = commit_info['sha']
        zipball_url = f'https://github.com/{author}/{repo_name}/archive/{commit_sha}.zip'
        console.log(f"[info]{t('upload.fetching_zip')}[/]")

        # Download the zipball
        response = requests.get(zipball_url)

        # Extract the content of the zipball into a temporary folder
        temp_path = os.path.join(os.path.dirname(os.getcwd()), 'temp_extracted')
        with ZipFile(BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(temp_path)
        console.log(f"[info]{t('upload.extracting')}[/]")


        # Move files from the temporary folder to the current folder
        for item in os.listdir(temp_path):
            item_path = os.path.join(temp_path, item)
            destination_path = os.path.join(local_path, item)
            shutil.move(item_path, destination_path)

        # Remove the temporary folder
        shutil.rmtree(temp_path)

        # Move all folder to main folder
        new_folder_name = f"{repo_name}-{commit_sha}"
        move_content(new_folder_name, ".")

        # Remove old temp folder
        shutil.rmtree(new_folder_name)

        console.log(f"[success]{t('upload.commit_success')}[/]")
    else:
        console.log(f"[error]{t('upload.commit_fail', status=response.status_code)}[/]")

def main_upload():

    repository_owner = 'brujorock'
    repository_name = 'sc-downloader'

    remote_version = get_remote_version()
    if remote_version is not None and remote_version == get_install_version():
        console.print(f"[success]{t('upload.already_updated')}[/]")
        return

    # Remove all old files, but keep the user's environment, git history,
    # downloaded content, local settings and Claude Code's own local state
    # (none of these come back from the repo zip since they're gitignored /
    # not tracked).
    keep_specific_items(".", [".venv", ".git", "downloads", ".claude"], ["data.json", "history.json"])

    download_and_extract_latest_commit(repository_owner, repository_name)

main_upload()
