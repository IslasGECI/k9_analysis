from k9_analysis import app, write_maya_nests_table

import os
import typer


def test_write_maya_nests_table():
    input_path = "tests/data/registros_rastros_de_gatos_k9_guadalupe_ISO8601.csv"
    output_path = "tests/data/maya_nests_table.csv"
    start_date = "2022-01-01"
    end_date = "2023-01-29"
    write_maya_nests_table(start_date, end_date, input_path, output_path)
    assert_path_exists(output_path)


def assert_path_exists(submission_path):
    assert os.path.exists(submission_path)
    os.remove(submission_path)
