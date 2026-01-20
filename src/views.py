
from utils import dataframe_to_json
from reports import spending_by_category

def main_page(df):
    report = spending_by_category(df, "Супермаркеты")
    return dataframe_to_json(report)
