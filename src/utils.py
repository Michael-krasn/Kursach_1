import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_transactions(path: str) -> pd.DataFrame:
    logger.info("Загрузка транзакций из Excel")
    df = pd.read_excel(path)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], errors="coerce")
    return df
