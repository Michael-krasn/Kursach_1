
import pandas as pd

def filter_successful(df: pd.DataFrame) -> pd.DataFrame:
    """Filter only successful transactions."""
    return df[df["Статус"] == "OK"]

def filter_period(df: pd.DataFrame, months: int) -> pd.DataFrame:
    """Filter transactions by period."""
    end = pd.Timestamp.now()
    start = end - pd.DateOffset(months=months)
    return df[(df["Дата операции"] >= start) & (df["Дата операции"] <= end)]

def calculate_sum(df: pd.DataFrame) -> float:
    """Calculate sum of payments."""
    return float(df["Сумма платежа"].sum())
