from utils.logger import get_module_logger
import sqlite3


class SQLite:

    def __init__(self):
        self.con = sqlite3.connect("./db/hpds.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.init_db()

    def init_db(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS ram ("
                         "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "created_at DATETIME DEFAULT current_timestamp, "
                         "total REAL NOT NULL, "
                         "free REAL NOT NULL, "
                         "used REAL NOT NULL);")
        self.con.commit()

    def fetch_query(self, query, params=()):
        try:
            result = self.cur.execute(query, params)
            return result.fetchall()
        except Exception as e:
            get_module_logger("SQLite").error(str(e))
            return None

    def commit_query(self, query, params=()):
        try:
            self.cur.execute(query, params)
            self.con.commit()
            return True
        except Exception as e:
            self.con.rollback()
            get_module_logger("SQLite").error(str(e))
            return False

    def close_connection(self):
        try:
            self.cur.close()
            self.con.close()
        except Exception as e:
            get_module_logger("SQLite").error(str(e))
