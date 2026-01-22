
import json
import pandas as pd
from datetime import datetime

def load_transactions(path: str) -> pd.DataFrame:
    """Load transactions from Excel file."""
    df = pd.read_excel(path)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], errors="coerce")
    return df

def dataframe_to_json(df: pd.DataFrame) -> str:
    """Convert DataFrame to JSON string."""
    return json.dumps(df.to_dict(orient="records"), ensure_ascii=False)

def get_now() -> datetime:
    """Return current datetime."""
    return datetime.now()
