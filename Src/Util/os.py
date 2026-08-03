# 24.01.24

# Import
import shutil, os, time
from Src.Util.i18n import t

def remove_folder(folder_path):
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
        except OSError as e:
            print(t("fs.remove_folder_error", path=folder_path, error=e))


def remove_file(file_path):
    if os.path.exists(file_path):
        time.sleep(1)

        try:
            os.remove(file_path)
        except OSError as e:
            print(t("fs.remove_file_error", path=file_path, error=e))
    else:
        print(t("fs.file_not_found", path=file_path))

    time.sleep(1)