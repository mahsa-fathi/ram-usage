from time import sleep
import psutil
import sys
import os

PROJECT_NAME = 'ram-usage/'
ROOT_DIR = str(str(os.path.realpath(__file__)).split(PROJECT_NAME)[0]) + PROJECT_NAME
sys.path.append(ROOT_DIR)


from utils.db_connect import SQLite
from utils.logger import get_module_logger


SQLITE = SQLite()


def insert_memory_to_db():
    """
    This function gets RAM info using psutil and inserts it into database
    """
    memory_total = psutil.virtual_memory().total / (1024.0 ** 2)
    memory_free = psutil.virtual_memory().free / (1024.0 ** 2)
    memory_used = psutil.virtual_memory().used / (1024.0 ** 2)
    if SQLITE.commit_query(query="INSERT INTO RAM (total, free, used) VALUES (?, ?, ?);",
                           params=(memory_total, memory_free, memory_used)):
        get_module_logger("Backend").info("inserted 1 row into db.")
    return memory_total, memory_free, memory_used


if __name__ == "__main__":
    while True:
        try:
            insert_memory_to_db()
        except Exception as e:
            get_module_logger("Backend").error(str(e))
        sleep(60)
