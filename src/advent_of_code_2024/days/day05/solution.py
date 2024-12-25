""" """

from advent_of_code_2024.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 5, year: int = 2024) -> None:
        super().__init__(day, year)

    def _parse_data(
        self: "DaySolution", input_data: str
    ) -> tuple[dict[int, list], list[list[int]]]:
        """ """
        rules, pages = input_data.strip().split("\n\n")
        rule_dict: dict[int, list] = {}
        for rule in rules.split("\n"):
            bef, nr = [int(x) for x in rule.split("|")]
            if bef not in rule_dict:
                rule_dict[bef] = []
            rule_dict[bef].append(nr)
        pages_lst = [[int(x) for x in ln.split(",")] for ln in pages.split("\n")]
        return rule_dict, pages_lst

    def correct_order(self, rules: dict[int, list], update: list, fix_wrong=False) -> int:
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                rule = rules.get(update[j], [])
                if update[i] in rule:
                    if fix_wrong:
                        update[i], update[j] = update[j], update[i]
                        return self.correct_order(rules, update, True)
                    else:
                        return 0

        return int(update[len(update) // 2])

    def _solve_part1(
        self: "DaySolution", parsed_data: tuple[dict[int, list], list[list[int]]]
    ) -> str:
        """ """
        rules, pages = parsed_data
        middle_pages = 0
        for ln in pages:
            middle_pages += self.correct_order(rules, ln, False)
        return str(middle_pages)

    def _solve_part2(
        self: "DaySolution", parsed_data: tuple[dict[int, list], list[list[int]]]
    ) -> str:
        rules, pages = parsed_data
        sol_1 = int(self._solve_part1(parsed_data))
        middle_pages = 0
        for ln in pages:
            middle_pages += self.correct_order(rules, ln, True)
        return str(middle_pages - sol_1)
