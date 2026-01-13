import pandas as pd
import logging
from typing import Optional
from .decorators import save_report

logger = logging.getLogger(__name__)


def _get_period(df: pd.DataFrame, date: Optional[str]):
    end_date = pd.to_datetime(date) if date else pd.Timestamp.now()
    start_date = end_date - pd.DateOffset(months=3)
    return df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= end_date)]


@save_report()
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: Optional[str] = None
) -> pd.DataFrame:
    logger.info(f"Анализ трат по категории: {category}")
    df = _get_period(transactions, date)
    return (
        df[df["Категория"] == category]
        .groupby("Категория")["Сумма платежа"]
        .sum()
        .reset_index()
    )


@save_report()
def spending_by_weekday(
    transactions: pd.DataFrame, date: Optional[str] = None
) -> pd.DataFrame:
    logger.info("Анализ трат по дням недели")
    df = _get_period(transactions, date)
    df["День недели"] = df["Дата операции"].dt.day_name()
    return df.groupby("День недели")["Сумма платежа"].mean().reset_index()


@save_report()
def spending_by_workday(
    transactions: pd.DataFrame, date: Optional[str] = None
) -> pd.DataFrame:
    logger.info("Анализ трат в рабочий и выходной день")
    df = _get_period(transactions, date)
    df["Тип дня"] = df["Дата операции"].dt.weekday.apply(
        lambda x: "Рабочий день" if x < 5 else "Выходной"
    )
    return df.groupby("Тип дня")["Сумма платежа"].mean().reset_index()
