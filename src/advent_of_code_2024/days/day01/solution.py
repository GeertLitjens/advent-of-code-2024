""" """

from advent_of_code_2024.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 1, year: int = 2024) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> tuple[list, list]:
        """ """
        l1, l2 = [], []
        for ln in input_data.strip().split("\n"):
            one, two = ln.split()
            l1.append(int(one))
            l2.append(int(two))
        return l1, l2

    def _solve_part1(self: "DaySolution", parsed_data: tuple[list, list]) -> str:
        """ """
        l1, l2 = parsed_data
        l1.sort()
        l2.sort()
        diffs = 0
        for i1, i2 in zip(l1, l2):
            diffs += abs(i1 - i2)
        return str(diffs)

    def _solve_part2(self: "DaySolution", parsed_data: tuple[list, list]) -> str:
        """ """
        sim = 0
        l1, l2 = parsed_data
        for n1 in l1:
            sim += n1 * l2.count(n1)
        return str(sim)
