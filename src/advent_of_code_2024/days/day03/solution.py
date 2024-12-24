""" """

import re

from advent_of_code_2024.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 3, year: int = 2024) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> str:
        """ """
        return input_data

    def _solve_part1(self: "DaySolution", parsed_data: str) -> str:
        """ """
        matches = re.findall(r"mul\((\d+),(\d+)\)", parsed_data)
        multi = 0
        for match in matches:
            multi += int(match[0]) * int(match[1])
        return str(multi)

    def _solve_part2(self: "DaySolution", parsed_data: str) -> str:
        """ """
        matches = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))", parsed_data)
        multi = 0
        do = True
        for i, j, k in matches:
            if i == "do()":
                do = True
            elif i == "don't()":
                do = False
            else:
                if do:
                    multi += int(j) * int(k)
        return str(multi)
