from fastapi import APIRouter

router = APIRouter(
    prefix="/api/report",
    tags=["report"]
)


@router.get("/health")

def health():

    return {
        "status": "report service running"
    }