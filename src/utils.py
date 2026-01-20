
import json
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_transactions(path: str) -> pd.DataFrame:
    logger.info("Loading Excel")
    df = pd.read_excel(path)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], errors="coerce")
    return df

def dataframe_to_json(df: pd.DataFrame) -> str:
    return json.dumps(df.to_dict(orient="records"), ensure_ascii=False)
