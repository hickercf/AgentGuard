from fastapi import APIRouter

from app.database.crud import get_reports


router = APIRouter(
    prefix="/api/history",
    tags=["history"]
)


@router.get("/")
def history():

    rows = get_reports()

    result = []

    for r in rows:

        result.append(
            {
                "id": r["id"],
                "task": r["task"],
                "report": r["report"],
                "time": r["created_at"]
            }
        )

    return result