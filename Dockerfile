# 1. ベースとなる環境（Python 3.11が入った軽量なLinux）
FROM python:3.11-slim

# 2. サーバー内の作業ディレクトリを「/app」に設定
WORKDIR /app

# 3. 必要なライブラリをインストール（fastapiとuvicorn）
# 本来はrequirements.txtを使いますが、今回は直接インストールします
RUN pip install --no-cache-dir fastapi uvicorn

# 4. ローカルの「main.py」を、サーバーの「/app」にコピー
COPY main.py .

# 5. コンテナが起動した時に実行するコマンド
# ポート8080で待ち受け、すべてのIPからの接続を許可（0.0.0.0）に設定
#CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "8080"]
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]