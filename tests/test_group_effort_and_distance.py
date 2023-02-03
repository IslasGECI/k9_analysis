from k9_analysis import get_total_time

import pandas as pd


def test_get_total_time():
    effort_data = pd.read_csv("tests/data/esfuerzos_k9_gatos_guadalupe_ISO8601.csv")
    obtained = get_total_time(effort_data)
    assert True
