
from .utils import load_transactions
from .views import main_page

def main() -> None:
    """Run application."""
    df = load_transactions("data/operations.xlsx")
    print(main_page(df))

if __name__ == "__main__":
    main()
