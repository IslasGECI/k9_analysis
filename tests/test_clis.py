from k9_analysis import (
    app,
    write_maya_nests_table,
    write_summary_of_marked_nests_by_year,
    write_total_time_and_distance_k9,
    write_total_time_and_distance_maya,
)

import json
import os
from typer.testing import CliRunner
import pandas as pd

runner = CliRunner()


def test_write_maya_nests_table():
    input_path = "tests/data/registros_rastros_de_gatos_k9_guadalupe_ISO8601.csv"
    output_path = "tests/data/maya_nests_table.csv"
    start_date = "2022-01-01"
    end_date = "2023-01-29"
    write_maya_nests_table(start_date, end_date, input_path, output_path)
    obtained = pd.read_csv(output_path)
    expected_columns = ["Unidad_K9", "Conteo"]
    assert (obtained.columns == expected_columns).all()
    assert_path_exists(output_path)


def test_write_summary_of_marked_nests_by_year():
    input_path = "tests/data/registros_rastros_de_gatos_k9_guadalupe_ISO8601.csv"
    output_path = "tests/data/maya_nests_table.csv"
    write_summary_of_marked_nests_by_year(input_path, output_path)
    obtained = pd.read_csv(output_path)
    expected_columns = ["Unidad_K9", "Temporada", "Conteo"]
    assert (obtained.columns == expected_columns).all()
    assert_path_exists(output_path)


def test_write_total_time_and_distance_k9():
    input_path = "tests/data/esfuerzos_k9_gatos_guadalupe_ISO8601.csv"
    output_path = "tests/data/total_time_and_distance_k9.csv"
    write_total_time_and_distance_k9(input_path, output_path)
    obtained = pd.read_csv(output_path)
    expected_columns = ["k9_name", "Total_distance", "Total_time"]
    assert (obtained.columns == expected_columns).all()
    assert_path_exists(output_path)


def test_write_total_time_and_distance_maya():
    input_path = "tests/data/input_k9_effort_data.csv"
    output_path = "tests/data/effort_summary.json"
    write_total_time_and_distance_maya(input_path, output_path)
    output_file = open(output_path, "r")
    json_string = output_file.read()
    dictionary = json.loads(json_string)
    assert dictionary["k9_name"] == "Maya"
    assert dictionary["Total_time"] == 120
    assert dictionary["Total_distance"] == 400
    assert_path_exists(output_path)


def assert_path_exists(submission_path):
    assert os.path.exists(submission_path)
    os.remove(submission_path)


def tests_app():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Commands:" in result.output

    result = runner.invoke(app, ["write-total-time-and-distance-maya", "--help"])
    assert "default: data/processed/total_time" in result.output
    assert "default: reports/non-tabular/maya_time_and_distance" in result.output

    result = runner.invoke(app, ["write-total-time-and-distance-k9", "--help"])
    assert " data/processed/esfuerzos_k9" in result.output
    assert "default: data/processed/total_time" in result.output
    assert "default: 2021-01-01" in result.output
    assert "default: 2022-12-31" in result.output

    result = runner.invoke(app, ["write-summary-of-marked-nests-by-year", "--help"])
    assert "default: data/processed/" in result.output
    assert "default: reports/tables/" in result.output

    result = runner.invoke(app, ["write-maya-nests-table", "--help"])
    assert "Options" in result.output
    assert "--start-date" in result.output
    assert "default: 2022-01-01" in result.output
    assert "default: 2023-01-29" in result.output
    assert "default: data/processed/" in result.output
    assert "default: reports/tables/" in result.output
