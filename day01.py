import sys
from typing import Literal


type Input = list[tuple[Literal["L", "R"], int]]


def parse(input: str) -> Input:
    def assert_literal(c):
        assert c == "L" or c == "R"
        return c

    return [
        (assert_literal(line[0]), int(line[1:])) for line in input.strip().split("\n")
    ]


def solve1(moves: Input):
    curr = 50
    ans = 0

    for direction, amount in moves:
        is_zero = 1 if curr == 0 else 0

        match direction:
            case "L":
                curr = (curr - amount) % 100
            case "R":
                curr = (curr + amount) % 100

        ans += is_zero

    if curr == 0:
        ans += 1

    return ans


def solve2(moves: Input):
    curr = 50
    ans = 0

    for direction, amount in moves:
        match direction:
            case "L":
                through_zero = abs((curr - amount) // 100)
                curr = (curr - amount) % 100
            case "R":
                through_zero = abs((((-curr) % 100) - amount) // 100)
                curr = (curr + amount) % 100

        ans += through_zero

    if curr == 0:
        ans += 1

    return ans


moves = parse(sys.stdin.read())
print(solve1(moves))
print(solve2(moves))
