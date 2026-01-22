
from .utils import dataframe_to_json
from .reports import spending_by_category
import pandas as pd

def main_page(df: pd.DataFrame) -> str:
    """Return main page JSON."""
    return dataframe_to_json(spending_by_category(df, "Супермаркеты"))
