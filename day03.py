import sys


type Input = list[list[int]]


def parse(input: str) -> Input:
    return [[int(d) for d in line] for line in input.strip().split("\n")]


def argmax(l: list) -> int:
    return max(range(len(l)), key=lambda i: l[i])


def solve(packs: Input, on_count: int):
    ans = 0

    for pack in packs:
        joltage = 0

        n = len(pack)
        i = -1
        for k in reversed(range(on_count)):
            i = argmax(pack[i + 1 : n - k]) + i + 1
            joltage += 10**k * pack[i]

        ans += joltage

    return ans


def solve1(packs: Input):
    return solve(packs, 2)


def solve2(packs: Input):
    return solve(packs, 12)


packs = parse(sys.stdin.read())
print(solve1(packs))
print(solve2(packs))
