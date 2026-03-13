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

    try:
        response = requests.post(

            settings.DEEPSEEK_URL,

            headers=headers,

            json=payload,

            timeout=60

        )

        response.raise_for_status()

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"LLM service error: {str(e)}"
    except (KeyError, IndexError) as e:
        return f"LLM response parsing error: {str(e)}"
