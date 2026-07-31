# 17.09.2023 -> 3.12.23

# Import
from rich.console import Console
from rich.prompt import Prompt
from Src.Util.theme import THEME
import logging

# Variable
console = Console(theme=THEME)
msg = Prompt(console=console)
SAVE_DEBUG = False

class ConfigurazioneLogger:
    def __init__(self, nome_file_log='debug.log'):
        self.nome_file_log = nome_file_log
        self.configura_logger()

    def configura_logger(self):
        if SAVE_DEBUG:
            logging.basicConfig(filename=self.nome_file_log, filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

config_logger = ConfigurazioneLogger()