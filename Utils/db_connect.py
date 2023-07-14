import sqlite3
import sys
import os

PROJECT_NAME = 'ram-usage/'
ROOT_DIR = str(str(os.path.realpath(__file__)).split(PROJECT_NAME)[0]) + PROJECT_NAME
sys.path.append(ROOT_DIR)

from utils.logger import get_module_logger


class SQLite:

    def __init__(self):
        self.con = sqlite3.connect(ROOT_DIR + "db/hpds.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.init_db()

    def init_db(self):
        """
        This function creates the ram table if it does not already exist
        """
        self.cur.execute("CREATE TABLE IF NOT EXISTS ram ("
                         "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "created_at DATETIME DEFAULT current_timestamp, "
                         "total REAL NOT NULL, "
                         "free REAL NOT NULL, "
                         "used REAL NOT NULL);")
        self.con.commit()

    def fetch_query(self, query, params=()):
        """
        This function inputs query and query params and executes the query
        It returns th fetched results if there were no errors
        """
        try:
            result = self.cur.execute(query, params)
            return result.fetchall()
        except Exception as e:
            get_module_logger("SQLite").error(str(e))
            return None

    def commit_query(self, query, params=()):
        """
        This function is used for queries that need to be committed such as insert and create table
        This function returns True when there were no errors and False otherwise
        """
        try:
            self.cur.execute(query, params)
            self.con.commit()
            return True
        except Exception as e:
            self.con.rollback()
            get_module_logger("SQLite").error(str(e))
            return False

    def close_connection(self):
        """
        This function close any connection to the database
        """
        try:
            self.cur.close()
            self.con.close()
        except Exception as e:
            get_module_logger("SQLite").error(str(e))
