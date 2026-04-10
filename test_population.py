import pytest
from population import read_population_file, sort_by_area, sort_by_population


# --- Fixtures ---

@pytest.fixture
def sample_records():
    return [
        {"country": "Ukraine", "area": 603550.0, "population": 43500000},
        {"country": "Vatican", "area": 0.44, "population": 825},
        {"country": "Canada", "area": 9984670.0, "population": 38200000},
    ]


@pytest.fixture
def txt_file(tmp_path):
    f = tmp_path / "data.txt"
    f.write_text(
        "Ukraine, 603550, 43500000\n"
        "Vatican, 0.44, 825\n"
        "Canada, 9984670, 38200000\n"
    )
    return str(f)


# --- Tests: read_population_file ---

def test_read_returns_correct_count(txt_file):
    assert len(read_population_file(txt_file)) == 3


def test_read_wrong_extension_raises(tmp_path):
    f = tmp_path / "data.csv"
    f.write_text("Ukraine, 603550, 43500000\n")
    with pytest.raises(ValueError):
        read_population_file(str(f))


def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_population_file("missing.txt")


# --- Tests: sort_by_area ---

@pytest.mark.parametrize("ascending,expected", [
    (True, "Vatican"),
    (False, "Canada"),
])
def test_sort_by_area_first(sample_records, ascending, expected):
    result = sort_by_area(sample_records, ascending=ascending)
    assert result[0]["country"] == expected


# --- Tests: sort_by_population ---

@pytest.mark.parametrize("ascending,expected", [
    (True, "Vatican"),
    (False, "Ukraine"),
])
def test_sort_by_population_first(sample_records, ascending, expected):
    result = sort_by_population(sample_records, ascending=ascending)
    assert result[0]["country"] == expected
