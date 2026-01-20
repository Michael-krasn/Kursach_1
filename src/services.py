
import pandas as pd

def filter_ok_transactions(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["Статус"] == "OK"]
