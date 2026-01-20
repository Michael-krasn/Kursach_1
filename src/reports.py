
import pandas as pd
from .decorators import save_report

@save_report()
def spending_by_category(df: pd.DataFrame, category: str, date=None) -> pd.DataFrame:
    return df[df["Категория"] == category].groupby("Категория")["Сумма платежа"].sum().reset_index()
