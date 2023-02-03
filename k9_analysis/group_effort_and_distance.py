import pandas as pd
from time import strptime


def get_total_time(effort_data: pd.DataFrame):
    pass


def interval_in_hours(string_time: str):
    time_format = strptime(string_time, "%H:%M:%S")
    return time_format.tm_hour + time_format.tm_min / 60 + time_format.tm_sec / 3600


def add_duration_in_hours_column(effort_data: pd.DataFrame):
    effort_data["Duration_hr"] = effort_data.Duracion.apply(interval_in_hours)
    return effort_data
