import sqlite3

from utils.miscellaneous import logging_logic


def dict_factory(cursor, row):
    save_dict = {}
    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]
    return save_dict

class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cur = self.connection.cursor()

    def start_sqlite(self):
        self.cur.row_factory = dict_factory
        #БД с пользователями
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS
        users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        in_search INTEGER,
        parther_id INTEGER,
        language TEXT,
        privat_photo_video INTEGER DEFAULT 0,
        alert INTEGER DEFAULT 0,
        age INTEGER,
        gender TEXT,
        time_registry DATETIME)""")

        self.connection.commit()

        logging_logic.logger.info("База данных подключена")


    def user_exists(self, user_id):
        self.cur.row_factory = dict_factory
        self.cur.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        result = self.cur.fetchone()
        return result is not None

    def add_user(self, user_id, username, lang, registry_time):
        self.cur.row_factory = dict_factory
        self.cur.execute("INSERT INTO users (user_id, username, language, time_registry) VALUES (?, ?, ?, ?)", (user_id, username, lang, registry_time))
        self.connection.commit()

        if lang == "ru":
            lang_text = "Русский"
        else:
            lang_text = "Узбекский"

        logging_logic.logger.info(f"Пользователь {username} добавлен в базу данных. Выбран язык '{lang_text}'")

    def get_user_by_id(self, user_id):
        self.cur.row_factory = dict_factory
        result = self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
        return result

    def update_users_column(self, user_id, column_name, new_value):
        self.cur.row_factory = dict_factory
        query = f"UPDATE users SET {column_name} = ? WHERE user_id = ?"
        self.cur.execute(query, (new_value, user_id))
        self.connection.commit()