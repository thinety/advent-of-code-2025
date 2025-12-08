import sys
from typing import Literal


type Input = list[list[Literal["S", "^", "."]]]


def parse(input: str) -> Input:
    def assert_literal(c):
        assert c == "S" or c == "^" or c == "."
        return c

    return [[assert_literal(c) for c in line] for line in input.strip().split("\n")]


def solve1(input: Input):
    n, m = len(input), len(input[0])

    splits = 0

    start_j = None
    for j in range(m):
        if input[0][j] == "S":
            start_j = j

    visited = [[False for _ in range(m)] for _ in range(n)]

    beams = []
    if start_j is not None:
        beams.append((0, start_j))

    def f(i, j):
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        beams.append((i, j))

    while beams:
        i, j = beams.pop()
        if visited[i][j]:
            continue
        visited[i][j] = True
        if input[i][j] == "^":
            splits += 1
            f(i + 1, j - 1)
            f(i + 1, j + 1)
        else:
            f(i + 1, j)

    return splits


def solve2(input: Input):
    n, m = len(input), len(input[0])

    start_j = None
    for j in range(m):
        if input[0][j] == "S":
            start_j = j

    visited = [[False for _ in range(m)] for _ in range(n)]
    timelines = [[0 for _ in range(m)] for _ in range(n)]

    beams = []
    if start_j is not None:
        beams.append((0, start_j))
        timelines[0][start_j] = 1

    while beams:
        beams_ = []

        def f(i, j, t):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            beams_.append((i, j))
            timelines[i][j] += t

        for i, j in beams:
            if visited[i][j]:
                continue
            visited[i][j] = True
            if input[i][j] == "^":
                f(i + 1, j - 1, timelines[i][j])
                f(i + 1, j + 1, timelines[i][j])
            else:
                f(i + 1, j, timelines[i][j])

        beams = beams_

    return sum(timelines[-1])


input = parse(sys.stdin.read())
print(solve1(input))
print(solve2(input))
