""" """

from advent_of_code_2024.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 2, year: int = 2024) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[list[int]]:
        """ """
        reports = [[int(x) for x in ln.split(" ")] for ln in input_data.strip().split("\n")]
        return reports

    def check_safety(self, a):
        diffs = [
            a[i + 1] - a[i] for i in range(len(a) - 1)
        ]  # build list of differences between consecutive pairs
        if (
            all(
                x < 0 and x in range(-3, 0) for x in diffs
            )  # all differences are negative and between -3 and -1
            or all(x > 0 and x in range(1, 4) for x in diffs)
        ):  # all differences are positive and between 1 and 3
            return True
        else:
            return False

    def _solve_part1(self: "DaySolution", parsed_data: list[list[int]]) -> str:
        """ """
        safe_report = 0
        for r in parsed_data:
            safe_report += self.check_safety(r)
        return str(safe_report)

    def _solve_part2(self: "DaySolution", parsed_data: list[list[int]]) -> str:
        """ """
        safe_report = 0
        for r in parsed_data:
            if self.check_safety(r):
                safe_report += 1
            else:
                for i in range(len(r)):
                    c_r = r.copy()
                    c_r.pop(i)
                    if self.check_safety(c_r):
                        safe_report += 1
                        break
        return str(safe_report)
