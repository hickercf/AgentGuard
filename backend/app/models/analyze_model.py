from pydantic import BaseModel


class AnalyzeRequest(BaseModel):

    task: str

    code: str