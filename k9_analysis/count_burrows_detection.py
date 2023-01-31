import pandas as pd


def count_nest(k9_data) -> int:
    start_date = "2022-01-01"
    end_date = "2023-01-29"
    k9_name = "Maya"
    only_maya = filter_k9(k9_name, k9_data)
    number_of_nest = filter_dates(only_maya, start_date, end_date)
    return filter_nest(number_of_nest)


def filter_dates(k9_data: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    filtered_df = k9_data.loc[(k9_data.Fecha <= end_date) & (k9_data.Fecha >= start_date)]
    return filtered_df


def filter_k9(k9_name: str, k9_data: pd.DataFrame) -> pd.DataFrame:
    return k9_data.loc[k9_data.Nombre_k9 == k9_name]


def filter_nest(k9_data: pd.DataFrame) -> pd.DataFrame:
    return k9_data.loc[k9_data.Tipo_de_rastro == "MD"]