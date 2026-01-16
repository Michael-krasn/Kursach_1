import json
from functools import wraps
from datetime import datetime


def save_report(name: str | None = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            filename = name or f"{func.__name__}_{datetime.now():%Y%m%d}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(result.to_dict(orient="records"), f, ensure_ascii=False)
            return result

        return wrapper

    return decorator
