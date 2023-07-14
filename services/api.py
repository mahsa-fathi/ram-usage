from fastapi import HTTPException, status, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
from utils.db_connect import SQLite
from utils.logger import get_module_logger
from utils.jsonify import jsonify_ram_results

app = FastAPI()

origins = ["http://localhost:8080"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

try:
    SQLITE = SQLite()
except Exception as e:
    get_module_logger('FastAPI').error(str(e))
    sys.exit()


@app.get("/ram/{no_min}")
def get_ram_usage(no_min: int):
    """
    This route is used for getting ram information
    no_min: integer
    return: json
    """
    res = SQLITE.fetch_query(query="SELECT created_at, total, free, used FROM ram ORDER BY created_at DESC LIMIT (?)",
                             params=(no_min,))
    if res is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return jsonify_ram_results(res)
