import pytest
from sort_s import sort_numbers


@pytest.mark.parametrize("input_string, expected_output", [
    ("5 2 8 1 9", [1, 2, 5, 8, 9]),
    ("10 -5 0 3 7", [-5, 0, 3, 7, 10]),
    ("1", [1]),
    ("", []),
    ("3 3 3 3", [3, 3, 3, 3]),
    ("-1 -10 -5 -2", [-10, -5, -2, -1]),
])
def test_sort_numbers(input_string, expected_output):
    assert sort_numbers(input_string) == expected_output


def test_sort_numbers_with_non_numeric_input():
    with pytest.raises(ValueError):
        sort_numbers("1 2 a 4")
