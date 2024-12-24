import pytest

from advent_of_code_2024.days.day01.solution import DaySolution  # type: ignore


@pytest.fixture
def day_testdata() -> str:
    return """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == "11"


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == "31"
