from k9_analysis import count_nest
import pandas as pd

k9_data = pd.read_csv("tests/data/registros_rastros_de_gatos_k9_guadalupe_ISO8601.csv")


def test_count_nest():
    obtained = count_nest(k9_data)
    obtained_type = type(obtained)
    expected_type = int
    assert obtained_type == expected_type
