import locale, time, glob
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
    log_filename = now.strftime("%Y-%m-%d_%H-%M-%S.log")

    # Получаем список файлов логов в текущей директории
    log_files = glob.glob("*.log")

    # Если у нас больше 5 логов, удаляем лишние
    if len(log_files) > 5:
        # Сортируем файлы по дате создания
        log_files.sort(key=os.path.getctime)

        # Удаляем лишние файлы
        for file_to_remove in log_files[:len(log_files)-5]:
            os.remove(file_to_remove)

    return log_filename
