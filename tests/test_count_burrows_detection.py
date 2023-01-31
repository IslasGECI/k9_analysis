from k9_analysis import count_nest, filter_dates
import pandas as pd

k9_data = pd.read_csv("tests/data/registros_rastros_de_gatos_k9_guadalupe_ISO8601.csv")


def test_count_nest():
    obtained = count_nest(k9_data)
    obtained_type = type(obtained)
    expected_type = int
    assert obtained_type == expected_type


def test_filter_dates():
    data = pd.DataFrame(
        {"Fecha": ["2022-12-01", "2022-12-31", "2023-01-31"], "Nombre_k9": ["Maya", "Maya", "Maya"]}
    )
    start_date = "2022-12-01"
    end_date = "2022-12-31"
    obtained = filter_dates(data, start_date, end_date)
    expected_rows = 2
    obtained_rows = len(obtained)
    assert obtained_rows == expected_rows
