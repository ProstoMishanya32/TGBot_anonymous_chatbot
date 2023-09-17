import logging as bot_logger

import colorlog
import os

from utils.miscellaneous.get_info import generate_log_filename

log_folder = "./data/logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Формат логгирования для файла
log_formatter_file = bot_logger.Formatter("%(levelname)s | %(asctime)s | %(filename)s:%(lineno)d | %(message)s")

# Формат логгирования для консоли с цветами
log_formatter_console = colorlog.ColoredFormatter(
    "%(purple)s%(levelname)s %(blue)s|%(purple)s %(asctime)s %(blue)s|%(purple)s %(filename)s:%(lineno)d %(blue)s|%(purple)s %(message)s%(red)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)

# Логгирование в файл в отдельной папке для каждой сессии
log_filename = os.path.join(log_folder, generate_log_filename())
file_handler = bot_logger.FileHandler(log_filename, "w", "utf-8")
file_handler.setFormatter(log_formatter_file)
file_handler.setLevel(bot_logger.DEBUG)  # Установите нужный уровень логгирования

# Логгирование в консоль
console_handler = bot_logger.StreamHandler()
console_handler.setFormatter(log_formatter_console)
console_handler.setLevel(bot_logger.DEBUG)  # Установите нужный уровень логгирования

# Создание логгера и установка уровня логгирования
logger = bot_logger.getLogger("skeynews")
logger.setLevel(bot_logger.DEBUG)  # Установите нужный уровень логгирования

# Добавление обработчиков (handlers) к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Функция для логгирования ошибок с информацией о типе и описании
def log_error_with_info(message, error_type, error_description):
    logger.error(f"{message} | Тип ошибки: {error_type} | Описание: {error_description}")