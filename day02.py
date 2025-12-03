import sys


type Input = list[tuple[int, int]]


def parse(input: str) -> Input:
    return [tuple(map(int, line.split("-"))) for line in input.strip().split(",")]


def solve1(ranges: Input):
    def is_invalid(id: int) -> bool:
        s = str(id)
        n = len(s)

        if n % 2 != 0:
            return False

        return s[: n // 2] == s[n // 2 :]

    ans = 0

    for a, b in ranges:
        for x in range(a, b + 1):
            if is_invalid(x):
                ans += x

    return ans


def solve2(ranges: Input):
    def is_invalid(id: int) -> bool:
        s = str(id)
        n = len(s)

        invalid = False
        for l in range(1, n):
            if n % l != 0:
                continue
            invalid_ = True
            i = l
            while i < n:
                invalid_ &= s[0:l] == s[i : i + l]
                i += l
            invalid |= invalid_

        return invalid

    ans = 0

    for a, b in ranges:
        for x in range(a, b + 1):
            if is_invalid(x):
                ans += x

    return ans


ranges = parse(sys.stdin.read())
print(solve1(ranges))
print(solve2(ranges))
