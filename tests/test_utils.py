import pandas as pd
from src.utils import dataframe_to_json


def test_dataframe_to_json():
    df = pd.DataFrame([{"a": 1}])
    assert '"a": 1' in dataframe_to_json(df)
