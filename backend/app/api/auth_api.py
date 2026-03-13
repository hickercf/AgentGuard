from fastapi import APIRouter


router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)


@router.post("/login")

def login(username: str, password: str):

    if username == "admin" and password == "admin":

        return {
            "token": "agent_guard_token"
        }

    return {
        "error": "login failed"
    }