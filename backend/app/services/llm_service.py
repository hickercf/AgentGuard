import requests

from app.config import settings


def call_llm(prompt):

    headers = {

        "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",

        "Content-Type": "application/json"

    }

    payload = {

        "model": "deepseek-chat",

        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]

    }

    response = requests.post(

        settings.DEEPSEEK_URL,

        headers=headers,

        json=payload

    )

    result = response.json()

    return result["choices"][0]["message"]["content"]