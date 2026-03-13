from fastapi import APIRouter
from app.database.crud import get_reports

router = APIRouter(
    prefix="/api/history",
    tags=["history"]
)


def safe_row_get(row, key):
    """
    安全访问 sqlite3.Row 对象：
    - 如果列存在，返回值
    - 如果列不存在，返回 None
    """
    try:
        return row[key]
    except (KeyError, IndexError):
        return None


@router.get("/")
def history():
    rows = get_reports()
    result = []

    for r in rows:
        # 打印调试列名，第一次用可以打开，确认字段名
        print("DEBUG row keys:", r.keys())
        print("DEBUG row content:", dict(r))

        record = {
            "id": safe_row_get(r, "id"),
            "task": safe_row_get(r, "task"),
            "report": safe_row_get(r, "report"),
            "time": safe_row_get(r, "created_at")  # 确保这里的列名和数据库字段一致
        }
        result.append(record)

    return result