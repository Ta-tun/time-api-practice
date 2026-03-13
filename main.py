# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime, timezone, timedelta
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# これを追加：どこからのアクセスも許可する設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 本番環境では特定のURLに絞るのがナウい（安全）
    allow_methods=["*"],
    allow_headers=["*"],
)

# 日本時間（JST）の定義
JST = timezone(timedelta(hours=+9))

@app.get("/")
def read_root():
    # 現在のUTC時刻を取得
    now_utc = datetime.now(timezone.utc)
    # UTCから日本時間（JST）に変換
    now_jst = now_utc.astimezone(JST)

    data = {
        "message": "Time Conversion API",
        "local_time_jst": now_jst.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_time      ": now_utc.strftime("%Y-%m-%d %H:%M:%S"),
        "unix_timestamp": int(now_utc.timestamp()) # おまけ：システムでよく使う数値形式
    }

    # indent=4 を指定して返す
    return JSONResponse(content=data, indent=4)