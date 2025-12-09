import sys
from math import prod


type Input = list[tuple[int, int, int]]


def parse(input: str) -> Input:
    def tuple_(t):
        t = tuple(t)
        assert len(t) == 3
        return t

    return [tuple_(map(int, line.split(","))) for line in input.strip().split("\n")]


def solve1(nodes: Input):
    n = len(nodes)

    def dist(p1, p2):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

    edges = []
    for u in range(n):
        for v in range(u):
            edges.append((dist(nodes[u], nodes[v]), u, v))

    edges = sorted(edges)

    representative = [u for u in range(n)]
    size = [1 for _ in range(n)]

    def find(u):
        if representative[u] == u:
            return u
        ans = find(representative[u])
        representative[u] = ans
        return ans

    def union(u, v):
        u = find(u)
        v = find(v)

        if u == v:
            return False

        if size[u] < size[v]:
            u, v = v, u

        representative[v] = u
        size[u] += size[v]
        return True

    for _, u, v in edges[:1000]:
        union(u, v)

    circuits = []
    for u in range(n):
        if find(u) == u:
            circuits.append(size[u])
    circuits = sorted(circuits, reverse=True)

    return prod(circuits[:3])


def solve2(nodes: Input):
    n = len(nodes)

    def dist(p1, p2):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

    edges = []
    for u in range(n):
        for v in range(u):
            edges.append((dist(nodes[u], nodes[v]), u, v))

    edges = sorted(edges)

    representative = [u for u in range(n)]
    size = [1 for _ in range(n)]

    def find(u):
        if representative[u] == u:
            return u
        ans = find(representative[u])
        representative[u] = ans
        return ans

    def union(u, v):
        u = find(u)
        v = find(v)

        if u == v:
            return False

        if size[u] < size[v]:
            u, v = v, u

        representative[v] = u
        size[u] += v
        return True

    for _, u, v in edges:
        if union(u, v):
            n -= 1
        if n == 1:
            x1, _, _ = nodes[u]
            x2, _, _ = nodes[v]
            return x1 * x2

    raise


nodes = parse(sys.stdin.read())
print(solve1(nodes))
print(solve2(nodes))
