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

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS
        interests(
        user_id INTEGER PRIMARY KEY,
        role_game INTEGER DEFAULT 0,
        mems INTEGER DEFAULT 0,
        loneliness INTEGER DEFAULT 0,
        flirting INTEGER DEFAULT 0,
        games INTEGER DEFAULT 0,
        music INTEGER DEFAULT 0,
        travels INTEGER DEFAULT 0,
        anime INTEGER DEFAULT 0,    
        movies INTEGER DEFAULT 0,   
        pets INTEGER DEFAULT 0, 
        books INTEGER DEFAULT 0,
        sport INTEGER DEFAULT 0)""")

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS
        chats(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user INTEGER NOT NULL,
        parther INTEGER NOT NULL)""")

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS
        queue(
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL)""")

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
        self.cur.execute("INSERT INTO interests (user_id) VALUES (?)", (user_id,))
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

    def get_interests_by_id(self, user_id):
        self.cur.row_factory = dict_factory
        result = self.cur.execute("SELECT * FROM interests WHERE user_id = ?", (user_id,)).fetchone()
        return result

    def update_users_column(self, user_id, column_name, new_value):
        self.cur.row_factory = dict_factory
        query = f"UPDATE users SET {column_name} = ? WHERE user_id = ?"
        self.cur.execute(query, (new_value, user_id))
        self.connection.commit()

    def update_interests_column(self, user_id, column_name, new_value):
        self.cur.row_factory = dict_factory
        query = f"UPDATE interests SET {column_name} = ? WHERE user_id = ?"
        self.cur.execute(query, (new_value, user_id))
        self.connection.commit()


    def update_interests_column(self, user_id, column_name, new_value):
        self.cur.row_factory = dict_factory
        query = f"UPDATE interests SET {column_name} = ? WHERE user_id = ?"
        self.cur.execute(query, (new_value, user_id))
        self.connection.commit()

    def update_all_interests(self, user_id, new_values):
        self.cur.row_factory = dict_factory
        query = """
            UPDATE interests
            SET 
                role_game = ?,
                mems = ?,
                loneliness = ?,
                flirting = ?,
                games = ?,
                music = ?,
                travels = ?,
                anime = ?,
                movies = ?,
                pets = ?,
                books = ?,
                sport = ?
            WHERE user_id = ?
        """
        values = (
            new_values,
            new_values,
            new_values,
            new_values,
            new_values,
            new_values,
            new_values,
            new_values,
            new_values,
            new_values,
            new_values,
            new_values,
            user_id
        )
        self.cur.execute(query, values)
        self.connection.commit()


    def add_queue(self, user_id):
        self.cur.row_factory = dict_factory

        self.cur.execute("INSERT INTO queue (user_id) VALUES (?)", (user_id,))
        self.connection.commit()

    def delete_queue(self, user_id):
        self.cur.row_factory = dict_factory

        self.cur.execute("DELETE FROM queue WHERE user_id = ?", (user_id,))
        self.connection.commit()

    def get_queue(self):
        self.cur.row_factory = dict_factory

        queue = self.cur.execute("SELECT * FROM queue").fetchmany(1)
        print(queue)
        if bool(len(queue)):
            for row in queue:
                return row['user_id']
        else:
            return False

    def create_chat(self, user_id, parther_id):
        self.cur.row_factory = dict_factory
        if parther_id != 0:
            self.cur.execute("INSERT INTO chats (user, parther) VALUES (?, ?)", (user_id, parther_id))
            return True
        else:
            return False
        self.connection.commit()


    def get_chat(self, user_id):
        self.cur.row_factory = dict_factory

        chat = self.cur.execute("SELECT * FROM chats WHERE user = ? OR parther = ?", (user_id, user_id))

        for i in chat:
            return [i['id'], i['user'] if i['user'] != user_id else i['parther']]

        return False

    def delete_chat(self, user_id):
        self.cur.row_factory = dict_factory

        self.cur.execute("DELETE FROM chats WHERE user = ? OR parther = ?", (user_id, user_id))
        self.connection.commit()
