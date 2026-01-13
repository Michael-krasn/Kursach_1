import json
import logging
from functools import wraps
from datetime import datetime

logger = logging.getLogger(__name__)


def save_report(filename: str | None = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            name = (
                filename
                or f"{func.__name__}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
            logger.info(f"Сохранение отчета {name}")
            with open(name, "w", encoding="utf-8") as f:
                json.dump(
                    result.to_dict(orient="records"), f, ensure_ascii=False, indent=2
                )
            return result

        return wrapper

    return decorator
