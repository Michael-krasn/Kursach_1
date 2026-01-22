
from unittest.mock import patch
import pandas as pd
from src.views import main_page

@patch("src.views.spending_by_category")
def test_main_page(mock_report):
    mock_report.return_value = pd.DataFrame([{"x": 1}])
    assert "x" in main_page(pd.DataFrame())
