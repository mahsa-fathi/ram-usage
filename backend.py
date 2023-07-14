from time import sleep
import asyncio
import psutil
import sys
import os

PROJECT_NAME = 'ram-usage/'
ROOT_DIR = str(str(os.path.realpath(__file__).replace('\\', '/')).split(PROJECT_NAME)[0]) + PROJECT_NAME
sys.path.append(ROOT_DIR)

from utils.db_connect import SQLite
from utils.logger import get_module_logger


SQLITE = SQLite()
SQLITE.init_db()
LOOP = asyncio.new_event_loop()
asyncio.set_event_loop(LOOP)


async def insert_memory_to_db():
    memory_total = psutil.virtual_memory().total / (1024.0 ** 2)
    memory_free = psutil.virtual_memory().free / (1024.0 ** 2)
    memory_used = psutil.virtual_memory().used / (1024.0 ** 2)
    if SQLITE.commit_query(query="INSERT INTO RAM (total, free, used) VALUES (?, ?, ?);",
                           params=(memory_total, memory_free, memory_used)):
        get_module_logger("Backend").info("inserted 1 row into db.")
    sleep(60)
    LOOP.create_task(insert_memory_to_db())


if __name__ == "__main__":
    LOOP.create_task(insert_memory_to_db())
    LOOP.run_forever()
