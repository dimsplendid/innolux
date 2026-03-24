from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import polars as pl
import io

app = FastAPI()

# 設定樣板路徑 (指向你的 frontend 資料夾)
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    # 讀取 Excel 內容
    contents = await file.read()
    df = pl.read_excel(io.BytesIO(contents))

    # 假設 Excel 前兩欄是數值，進行相加
    # 這裡示範：新增一欄 'Result' 為前兩欄之和
    cols = df.columns
    df_result = df.with_columns(
        (pl.col(cols[0]) + pl.col(cols[1])).alias("Result")
    )
    # 轉成 HTML 表格回傳給 HTMX
    table_html = df_result.to_pandas().to_html(classes="table", index=False)
    
    return HTMLResponse(content=f"<h3>計算結果：</h3>{table_html}")