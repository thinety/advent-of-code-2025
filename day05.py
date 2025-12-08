import sys
from bisect import bisect_right


type Input = tuple[list[tuple[int, int]], list[int]]


def parse(input: str) -> Input:
    ranges, ids = input.strip().split("\n\n")
    ranges = [
        (int(a), int(b)) for a, b in map(lambda l: l.split("-"), ranges.split("\n"))
    ]
    ids = [int(x) for x in ids.split("\n")]
    return ranges, ids


def solve1(input: Input):
    ranges, ids = input

    ranges_ = sorted(ranges)
    ranges: list[tuple[int, int]] = []
    last_a, last_b = ranges_[0]
    for a, b in ranges_[1:]:
        if a > last_b + 1:
            ranges.append((last_a, last_b))
            last_a, last_b = a, b
        else:
            last_b = max(last_b, b)
    ranges.append((last_a, last_b))

    ans = 0
    for id in ids:
        i = bisect_right(ranges, id, key=lambda r: r[0])
        if i == 0:
            continue
        a, b = ranges[i - 1]
        if a <= id <= b:
            ans += 1

    return ans


def solve2(input: Input):
    ranges, _ = input

    ranges_ = sorted(ranges)
    ranges: list[tuple[int, int]] = []
    last_a, last_b = ranges_[0]
    for a, b in ranges_[1:]:
        if a > last_b + 1:
            ranges.append((last_a, last_b))
            last_a, last_b = a, b
        else:
            last_b = max(last_b, b)
    ranges.append((last_a, last_b))

    ans = 0
    for a, b in ranges:
        ans += b - a + 1

    return ans


input = parse(sys.stdin.read())
print(solve1(input))
print(solve2(input))
