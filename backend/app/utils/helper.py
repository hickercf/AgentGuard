import json


def safe_json(data):

    try:
        return json.dumps(data, ensure_ascii=False, indent=2)
    except:
        return str(data)


def truncate(text, length=500):

    if len(text) <= length:
        return text

    return text[:length] + "..."