import sys
import os

# 将 backend 目录加入模块搜索路径（必须在 app.* 导入之前）
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.analyze_api import router as analyze_router
from app.api.report_api import router as report_router
from app.api.history_api import router as history_router
from app.api.auth_api import router as auth_router
from app.database.init_db import init_database

# 启动时自动初始化数据库
init_database()

app = FastAPI(
    title="Agent Guard",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(analyze_router)
app.include_router(report_router)
app.include_router(history_router)
app.include_router(auth_router)


@app.get("/")
def root():

    return {
        "status": "Agent Guard Running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
