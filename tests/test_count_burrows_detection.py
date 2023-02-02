from k9_analysis import (
    extract_year,
    filter_nest_traces_by_k9_and_interval,
    filter_dates,
    filter_k9,
    filter_nest,
    make_summary_maya_2022_number_of_nest_marked,
    make_summary_of_marked_nests_by_year,
)
import pandas as pd

k9_data = pd.read_csv("tests/data/registros_rastros_de_gatos_k9_guadalupe_ISO8601.csv")


def test_make_summary_maya_2022_number_of_nest_marked():
    obtained = make_summary_maya_2022_number_of_nest_marked(k9_data)
    obtained_rows = len(obtained)
    expected_rows = 1
    assert obtained_rows == expected_rows
    obtained_columns = obtained.columns
    obtained_number_columns = len(obtained_columns)
    expected_number_columns = 2
    assert obtained_number_columns == expected_number_columns, "Número de columnas"
    expected_columns = ["Unidad_K9", "Conteo"]
    assert (obtained_columns == expected_columns).all(), "Nombres de las columnas"
    assert obtained.Conteo[0] == 19

    start_date = "2021-01-01"
    end_date = "2021-12-31"
    obtained = make_summary_maya_2022_number_of_nest_marked(k9_data, start_date, end_date)
    expected_nests = 7
    obtained_nests = obtained.Conteo[0]
    assert obtained_nests == expected_nests


def test_filter_nest_traces_by_k9_and_interval():
    start_date = "2022-01-01"
    end_date = "2023-01-29"
    obtained = filter_nest_traces_by_k9_and_interval(k9_data, start_date, end_date)
    obtained_rows = len(obtained)
    expected_rows = 20
    assert obtained_rows == expected_rows


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
    obtained_dates = obtained.Fecha
    expected_dates = ["2022-12-01", "2022-12-31"]
    assert (obtained_dates == expected_dates).all()


def test_filter_k9():
    data = pd.DataFrame(
        {"Fecha": ["2022-12-01", "2022-12-31", "2023-01-31"], "Nombre_k9": ["Maya", "Thor", "Maya"]}
    )
    obtained = filter_k9("Maya", data)
    expected_rows = 2
    obtained_rows = len(obtained)
    assert obtained_rows == expected_rows


def test_filter_nest():
    data = pd.DataFrame(
        {
            "Fecha": ["2022-12-01", "2022-12-31", "2023-01-31"],
            "Nombre_k9": ["Maya", "Thor", "Maya"],
            "Tipo_de_rastro": ["MD", "PL", "E1"],
        }
    )
    obtained = filter_nest(data)
    expected_rows = 1
    obtained_rows = len(obtained)
    assert obtained_rows == expected_rows


def test_extract_year():
    k9_df = pd.DataFrame(
        {
            "Fecha": ["2022-12-01", "2022-12-31", "2023-01-31"],
            "Nombre_k9": ["Maya", "Thor", "Maya"],
            "Tipo_de_rastro": ["MD", "PL", "E1"],
        }
    )
    obtained = extract_year(k9_df)
    expected_column = "Temporada"
    assert expected_column in obtained.columns
    expected_years = ["2022", "2022", "2023"]
    assert (obtained.Temporada == expected_years).all()


def tests_make_summary_of_marked_nests_by_year():
    k9_df = pd.DataFrame(
        {
            "Fecha": ["2021-04-13", "2022-12-01", "2022-12-31", "2023-01-31", "2023-01-31"],
            "Nombre_k9": ["Maya", "Maya", "Thor", "Maya", "Maya"],
            "Tipo_de_rastro": ["E2", "MD", "PL", "MD", "MD"],
        }
    )
    obtained = make_summary_of_marked_nests_by_year(k9_df)
    expected_rows = 2
    assert len(obtained) == expected_rows
    print(make_summary_of_marked_nests_by_year(k9_data))
    assert False
