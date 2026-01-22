
import pandas as pd
import pytest
from src.services import filter_successful, calculate_sum

@pytest.mark.parametrize(
    "statuses,expected",
    [
        (["OK", "FAILED"], 1),
        (["OK", "OK"], 2),
    ],
)
def test_filter_successful(statuses, expected):
    df = pd.DataFrame({"Статус": statuses, "Сумма платежа": [100] * len(statuses)})
    assert len(filter_successful(df)) == expected

def test_calculate_sum():
    df = pd.DataFrame({"Сумма платежа": [100, 200]})
    assert calculate_sum(df) == 300
