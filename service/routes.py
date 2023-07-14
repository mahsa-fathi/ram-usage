from . import app, sqlite
from fastapi import HTTPException
from utils.jsonify import jsonify_ram_results


@app.get("/ram/{no_min}")
def get_ram_usage(no_min: int):
    res = sqlite.fetch_query(query="SELECT created_at, total, free, used FROM ram ORDER BY created_at DESC LIMIT (?)",
                             params=(no_min,))
    if res in None:
        raise HTTPException(status_code=404, detail="Number of minutes range is not acceptable.")
    return jsonify_ram_results(res)


@app.get("/version/")
def get_version():
    return 1.0


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8088)
