""" """

from advent_of_code_2024.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 4, year: int = 2024) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> list[list[str]]:
        """ """
        wsk = [[x for x in ln] for ln in input_data.strip().split("\n")]
        return wsk

    def check_xmas(self: "DaySolution", wsk: list[list[str]], pos: tuple[int, int]):
        nr_xmas = 0
        lts = ["X", "M", "A", "S"]
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            for ind in range(1, 4):
                cur_pos = (pos[0] + ind * dir[0], pos[1] + ind * dir[1])
                if (
                    cur_pos[0] > (len(wsk) - 1)
                    or cur_pos[1] > (len(wsk[0]) - 1)
                    or cur_pos[0] < 0
                    or cur_pos[1] < 0
                ):
                    break
                if wsk[cur_pos[0]][cur_pos[1]] == lts[ind]:
                    if ind == 3:
                        nr_xmas += 1
                else:
                    break
        return nr_xmas

    def check_mas(self: "DaySolution", wsk: list[list[str]], pos: tuple[int, int]):
        if pos[0] >= (len(wsk) - 1) or pos[1] >= (len(wsk[0]) - 1) or pos[0] <= 0 or pos[1] <= 0:
            return False
        word_1 = wsk[pos[0] - 1][pos[1] - 1] + "A" + wsk[pos[0] + 1][pos[1] + 1]
        word_2 = wsk[pos[0] + 1][pos[1] - 1] + "A" + wsk[pos[0] - 1][pos[1] + 1]
        return word_1 in ["SAM", "MAS"] and word_2 in ["SAM", "MAS"]

    def _solve_part1(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        x_posses = []
        for i, row in enumerate(parsed_data):
            for j, col in enumerate(row):
                if col == "X":
                    x_posses.append((i, j))
        nr_xmas = 0
        for x_pos in x_posses:
            nr_xmas += self.check_xmas(parsed_data, x_pos)
        return str(nr_xmas)

    def _solve_part2(self: "DaySolution", parsed_data: list[list[str]]) -> str:
        """ """
        a_posses = []
        for i, row in enumerate(parsed_data):
            for j, col in enumerate(row):
                if col == "A":
                    a_posses.append((i, j))
        nr_mas = 0
        for a_pos in a_posses:
            nr_mas += self.check_mas(parsed_data, a_pos)
        return str(nr_mas)
