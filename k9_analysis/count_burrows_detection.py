import pandas as pd


def count_nest(k9_data) -> int:
    return 0


def filter_dates(k9_data: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    filtered_df = k9_data.loc[(k9_data.Fecha <= end_date) & (k9_data.Fecha >= start_date)]
    return filtered_df


def filter_k9(k9_name: str, k9_data: pd.DataFrame) -> pd.DataFrame:
    return k9_data.loc[k9_data.Nombre_k9 == k9_name]
