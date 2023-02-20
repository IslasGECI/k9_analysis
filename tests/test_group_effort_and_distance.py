from k9_analysis import (
    add_duration_in_hours_column,
    interval_in_hours,
    make_summary_of_effort_and_distance,
)

import pandas as pd
import pytest
import numpy as np


effort_data = pd.read_csv("tests/data/esfuerzos_k9_gatos_guadalupe_ISO8601.csv")


def tests_interval_in_hours():
    string_time = "01:36:28"
    obtained = interval_in_hours(string_time)
    expected = 1.60777
    assert obtained == pytest.approx(expected, 0.01)
    string_time = "00:00:00"
    obtained = interval_in_hours(string_time)
    expected = 0
    assert obtained == pytest.approx(expected, 0.01)


def test_add_duration_in_hours_column():
    obtained_df = add_duration_in_hours_column(effort_data)
    expected_column = "Duration_hr"
    assert expected_column in obtained_df.columns
    expected_row = 0.9077
    assert obtained_df.Duration_hr.iloc[9] == pytest.approx(expected_row, 0.01)


effort_df = pd.DataFrame(
    {
        "Fecha": [
            "2021-04-13",
            "2022-12-01",
            "2022-12-31",
            "2023-01-31",
            "2023-01-31",
            "2020-12-04",
        ],
        "Nombre_k9": ["Maya", "Maya", "Thor", "Maya", "Maya", "Thor"],
        "Duracion": ["01:36:28", "03:33:28", "02:26:07", "00:58:24", "00:00:00", np.nan],
        "Distancia": [5.9, 2, 1, 1, 1.1, 1],
    }
)


def tests_make_summary_of_effort_and_distance():
    obtained_summary = make_summary_of_effort_and_distance(effort_df)
    print(obtained_summary)
    obtained_k9s = len(obtained_summary.Total_distance)
    expected_k9s = 2
    assert obtained_k9s == expected_k9s
    expected_maya_total_distance = 10
    obtained_maya_total_distance = obtained_summary.Total_distance.loc["Maya"]
    assert obtained_maya_total_distance == expected_maya_total_distance

    expected_thor_total_time = 2.435
    obtained_thor_total_time = obtained_summary.Total_time.loc["Thor"]
    assert obtained_thor_total_time == pytest.approx(expected_thor_total_time, 0.01)


def tests_make_summary_of_effort_and_distance_with_arguments():
    start_date = "2021-01-01"
    end_date = "2022-12-31"
    obtained_summary = make_summary_of_effort_and_distance(effort_df, start_date, end_date)
    expected_maya_total_distance = 7.9
    obtained_maya_total_distance = obtained_summary.Total_distance.loc["Maya"]
    assert obtained_maya_total_distance == expected_maya_total_distance

    expected_thor_total_time = 2.435
    obtained_thor_total_time = obtained_summary.Total_time.loc["Thor"]
    assert obtained_thor_total_time == pytest.approx(expected_thor_total_time, 0.01)
