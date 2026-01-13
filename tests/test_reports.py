import pandas as pd
from src.reports import spending_by_category, spending_by_weekday, spending_by_workday


def test_spending_by_category(transactions_df):
    result = spending_by_category(transactions_df, "Супермаркеты", "2025-02-15")
    assert result.iloc[0]["Сумма платежа"] == 2300


def test_spending_by_weekday(transactions_df):
    result = spending_by_weekday(transactions_df, "2025-02-15")
    assert isinstance(result, pd.DataFrame)


def test_spending_by_workday(transactions_df):
    result = spending_by_workday(transactions_df, "2025-02-15")
    assert set(result["Тип дня"]).issubset({"Рабочий день", "Выходной"})
