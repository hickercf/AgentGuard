from pydantic import BaseModel


class ReportModel(BaseModel):

    task_id: str
    user_id: str

    security: str
    legal: str
    behavior: str

    prompt_attack: str

    static_scan: list

    risk_score: int
    risk_level: str

    repair_code: str