import sys
from typing import Literal


type Input = list[list[Literal["@", "."]]]


def parse(input: str) -> Input:
    def assert_literal(c):
        assert c == "@" or c == "."
        return c

    return [[assert_literal(c) for c in line] for line in input.strip().split("\n")]


def solve1(rolls: Input):
    n = len(rolls)
    m = len(rolls[0])

    def neighbors(i, j):
        ans = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                ii = i + di
                jj = j + dj
                if ii < 0 or ii >= n:
                    continue
                if jj < 0 or jj >= m:
                    continue
                if rolls[ii][jj] == "@":
                    ans += 1
        return ans

    ans = 0
    for i in range(n):
        for j in range(m):
            if rolls[i][j] == "@" and neighbors(i, j) < 4:
                ans += 1
    return ans


def solve2(rolls: Input):
    n = len(rolls)
    m = len(rolls[0])

    def neighbors(i, j):
        ans = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                ii = i + di
                jj = j + dj
                if ii < 0 or ii >= n:
                    continue
                if jj < 0 or jj >= m:
                    continue
                if rolls[ii][jj] == "@":
                    ans += 1
        return ans

    ans = 0
    can_be_removed = []
    while True:
        for i in range(n):
            for j in range(m):
                if rolls[i][j] == "@" and neighbors(i, j) < 4:
                    can_be_removed.append((i, j))
        if not can_be_removed:
            break
        for i, j in can_be_removed:
            rolls[i][j] = "."
            ans += 1
        can_be_removed = []

    return ans


rolls = parse(sys.stdin.read())
print(solve1(rolls))
print(solve2(rolls))
