# main.py
from fastapi import FastAPI
from datetime import datetime, timezone, timedelta

app = FastAPI()

# 日本時間（JST）の定義
JST = timezone(timedelta(hours=+9))

@app.get("/")
def read_root():
    # 現在のUTC時刻を取得
    now_utc = datetime.now(timezone.utc)
    # UTCから日本時間（JST）に変換
    now_jst = now_utc.astimezone(JST)

    return {
        "message": "Time Conversion API",
        "local_time_jst": now_jst.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_time      ": now_utc.strftime("%Y-%m-%d %H:%M:%S"),
        "unix_timestamp": int(now_utc.timestamp()) # おまけ：システムでよく使う数値形式
    }