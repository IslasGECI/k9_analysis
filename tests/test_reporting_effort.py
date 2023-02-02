from k9_analysis import ReportingEffort


data_paths = dict(
    k9_effort_path="tests/data/input_k9_effort_data.csv",
)
obtained_report = ReportingEffort(data_paths=data_paths)


def test_init_ReportingEffort():
    obtained_report = ReportingEffort(data_paths=data_paths)
    obtained_class = obtained_report.__class__.__name__
    expected_class = "ReportingEffort"
    assert obtained_class == expected_class


def test_get_maya_effort_distance():
    obtained_maya_calculate_total_time = obtained_report.get_maya_effort_distance()
    expected_total_time = 400
    assert obtained_maya_calculate_total_time == expected_total_time


def test_get_maya_effort_time():
    obtained_total_time = obtained_report.get_maya_effort_time()
    expected_total_time = 120
    assert obtained_total_time == expected_total_time
