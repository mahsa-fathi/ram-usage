from fastapi import FastAPI
import sys
import os

PROJECT_NAME = 'ram-usage/'
ROOT_DIR = str(str(os.path.realpath(__file__).replace('\\', '/')).split(PROJECT_NAME)[0]) + PROJECT_NAME
sys.path.append(ROOT_DIR)

app = FastAPI()

from service import routes
from utils.db_connect import SQLite
from utils.logger import get_module_logger

try:
    sqlite = SQLite()
    sqlite.init_db()
except Exception as e:
    get_module_logger('FastAPI').error(str(e))
    sys.exit(4)

get_module_logger('FastAPI').info("Service Initialized.")
