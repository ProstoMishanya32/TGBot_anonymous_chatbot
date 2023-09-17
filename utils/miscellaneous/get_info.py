import locale
import time
from datetime import datetime


def get_real_time():
    # Устанавливаем русскую локаль
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return time


def get_unix():
    unique_number = int(time.time())
    return unique_number


def generate_log_filename():
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S.log")

