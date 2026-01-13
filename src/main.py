import logging
from utils import load_transactions
from reports import spending_by_category, spending_by_weekday, spending_by_workday

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    df = load_transactions("data/operations.xlsx")
    spending_by_category(df, "Супермаркеты")
    spending_by_weekday(df)
    spending_by_workday(df)
