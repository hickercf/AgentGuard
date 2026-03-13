from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.analyze_api import router as analyze_router
from app.api.report_api import router as report_router
from app.api.history_api import router as history_router


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


@app.get("/")
def root():

    return {
        "status": "Agent Guard Running"
    }