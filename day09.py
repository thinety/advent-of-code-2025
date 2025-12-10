from bisect import bisect_left
import sys


type Input = list[tuple[int, int]]


def parse(input: str) -> Input:
    def tuple_(t):
        t = tuple(t)
        assert len(t) == 2
        return t

    return [tuple_(map(int, line.split(","))) for line in input.strip().split("\n")]


def solve1(input: Input):
    ans = 0
    for i, (x1, y1) in enumerate(input):
        for x2, y2 in input[i + 1 :]:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            ans = max(ans, area)
    return ans


def solve2(input: Input):
    all_x = sorted(set(x for x, _ in input))
    all_y = sorted(set(y for _, y in input))

    def mapx(x):
        i = bisect_left(all_x, x)
        return 2 * i + (1 if i < len(all_x) and all_x[i] == x else 0)

    def mapy(y):
        i = bisect_left(all_y, y)
        return 2 * i + (1 if i < len(all_y) and all_y[i] == y else 0)

    maxx = 2 * len(all_x) + 1
    maxy = 2 * len(all_y) + 1

    # 0 for outside, 1 for border, 2 for inside
    valid = [[2 for _ in range(maxy)] for _ in range(maxx)]

    n = len(input)
    for i in range(n):
        x1, y1 = input[i]
        x2, y2 = input[(i + 1) % n]

        x1, x2, y1, y2 = mapx(x1), mapx(x2), mapy(y1), mapy(y2)
        x1, x2, y1, y2 = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)

        if x1 == x2:
            for y in range(y1, y2 + 1):
                valid[x1][y] = 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                valid[x][y1] = 1
        else:
            raise

    flood = [(0, 0)]
    while flood:
        x, y = flood.pop()
        if x < 0 or x >= maxx or y < 0 or y >= maxy:
            continue
        if valid[x][y] != 2:
            continue
        valid[x][y] = 0
        flood.append((x - 1, y))
        flood.append((x + 1, y))
        flood.append((x, y - 1))
        flood.append((x, y + 1))

    rectangles = []
    for i, (x1, y1) in enumerate(input):
        for x2, y2 in input[i + 1 :]:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

            x1_, x2_, y1_, y2_ = mapx(x1), mapx(x2), mapy(y1), mapy(y2)
            x1_, x2_, y1_, y2_ = (
                min(x1_, x2_),
                max(x1_, x2_),
                min(y1_, y2_),
                max(y1_, y2_),
            )

            rectangles.append((area, x1_, y1_, x2_, y2_))
    rectangles = sorted(rectangles, reverse=True)

    for area, x1, y1, x2, y2 in rectangles:
        ok = True
        for x in range(x1, x2 + 1):
            ok &= valid[x][y1] != 0
            ok &= valid[x][y2] != 0
        for y in range(y1 + 1, y2):
            ok &= valid[x1][y] != 0
            ok &= valid[x2][y] != 0
        if ok:
            return area

    return 0


input = parse(sys.stdin.read())
print(solve1(input))
print(solve2(input))
