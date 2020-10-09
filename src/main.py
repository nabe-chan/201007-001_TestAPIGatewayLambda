from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from mangum import Mangum
import uvicorn

import pathlib

#
# FastAPIフレームワークのインスタンス化
#
# app server (uvicorn) からコールされる関数
#
app = FastAPI()

#
# jinja2のテンプレートインスタンス生成
#
# 相対パスで指定
# Lambda = root is uploaded zip file name.
# local uvicorn = root is parent directory of main.py.
#
PATH_TEMPLATES = str(
    pathlib.Path(__file__).resolve().parent / "templates"
)
templates = Jinja2Templates(directory=PATH_TEMPLATES)

#
# Controller 定義
# /
#
@app.get("/", response_class=HTMLResponse)
def index(request:Request):
    msg = "This is variable message."
    context = {
        "request":request,
        "message":msg
    }
    return templates.TemplateResponse(
        "index.html",
        context
    )

#
# ルーティング定義
#
#app.add_api_route("/", index)

#
# Mangumフレームワークのインスタンス化
#
# lambdaのhandlerに指定する関数
#
handler = Mangum(app)

# 
# Run FastAPI/Mangum Code using uvicorn
#
# ローカルテスト用 (lambda実行時はcallされない)
# コンソールで [$ uvicorn main:app --reload]でも可
# 
if __name__ == '__main__':
    uvicorn.run(app=app)
