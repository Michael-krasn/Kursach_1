import pytest
import pandas as pd


@pytest.fixture
def transactions_df():
    data = {
        "Дата операции": pd.to_datetime(
            [
                "2025-01-10",
                "2025-01-11",
                "2025-01-12",
                "2025-02-01",
                "2025-02-02",
            ]
        ),
        "Категория": [
            "Супермаркеты",
            "Супермаркеты",
            "Кафе",
            "Кафе",
            "Супермаркеты",
        ],
        "Сумма платежа": [1000, 500, 300, 700, 800],
    }
    return pd.DataFrame(data)
