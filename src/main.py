
from utils import load_transactions
from views import main_page

if __name__ == "__main__":
    df = load_transactions("data/operations.xlsx")
    print(main_page(df))
