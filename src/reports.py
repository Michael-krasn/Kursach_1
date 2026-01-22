
import pandas as pd
from typing import Optional
from .services import filter_successful, filter_period

def spending_by_category(df: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Calculate spending by category."""
    df = filter_successful(df)
    df = filter_period(df, 3)
    return df[df["Категория"] == category].groupby("Категория")["Сумма платежа"].sum().reset_index()
