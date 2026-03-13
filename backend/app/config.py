import os


class Settings:

    PROJECT_NAME = "Agent Guard"

    API_VERSION = "1.0"

    DEEPSEEK_API_KEY = os.getenv(
        "DEEPSEEK_API_KEY",
        "sk-a0e2cb80653840a690811a88a5b35e61"
    )

    DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"


settings = Settings()