import sys
from typing import Literal


type Input = tuple[
    list[list[list[Literal["#", "."]]]], list[tuple[int, int, list[int]]]
]


def parse(input: str) -> Input:
    [*presents, regions] = input.strip().split("\n\n")

    def assert_literal(c):
        assert c == "#" or c == "."
        return c

    presents = [
        [[assert_literal(c) for c in line] for line in present.split("\n")[1:]]
        for present in presents
    ]

    def parse_region(region):
        [size, *presents] = region.split()
        [w, h] = size[:-1].split("x")

        return int(w), int(h), list(map(int, presents))

    regions = [parse_region(region) for region in regions.split("\n")]

    return presents, regions


def solve1(input: Input):
    presents, regions = input

    ans = 0

    # maybe it's enough to test for the upper bound?
    present_upper_bounds = [len(p) * len(p[0]) for p in presents]
    for w, h, required_presents in regions:
        required_size_upper_bound = sum(
            size * amount
            for size, amount in zip(present_upper_bounds, required_presents)
        )
        if w * h >= required_size_upper_bound:
            ans += 1

    return ans


input = parse(sys.stdin.read())
print(solve1(input))
