import logging

logger = logging.getLogger(__name__) #Создание объекта логгера
logger.setLevel(logging.DEBUG)


# Создаем файл логов
handler = logging.FileHandler("./data/logs/logs.log", encoding="utf-8")
handler.setLevel(logging.DEBUG)

#Формат для записи логов

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

#Добавление файл логов в логгер
logger.addHandler(handler)


