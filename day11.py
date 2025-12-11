import sys


type Input = dict[str, list[str]]


def parse(input: str) -> Input:
    g = {}

    for line in input.strip().split("\n"):
        [u, *vs] = line.split()
        u = u[:-1]

        if u not in g:
            g[u] = []
        for v in vs:
            g[u].append(v)
            if v not in g:
                g[v] = []

    return g


def solve1(g: Input):
    reverse_g = {u: [] for u in g}
    for u, vs in g.items():
        for v in vs:
            reverse_g[v].append(u)

    def get_topoorder(u0):
        postorder = []
        visited = set()

        def go(u):
            if u in visited:
                return
            visited.add(u)

            for v in g[u]:
                go(v)

            postorder.append(u)

        go(u0)

        return list(reversed(postorder))

    def get_dp(u0):
        topoorder = get_topoorder(u0)

        dp = {u0: 1}

        for u in topoorder[1:]:
            dp[u] = 0

            for v in reverse_g[u]:
                if v not in dp:
                    continue

                dp[u] += dp[v]

        return dp

    dp = get_dp("you")
    return dp["out"]


def solve2(g: Input):
    reverse_g = {u: [] for u in g}
    for u, vs in g.items():
        for v in vs:
            reverse_g[v].append(u)

    def get_topoorder(u0):
        postorder = []
        visited = set()

        def go(u):
            if u in visited:
                return
            visited.add(u)

            for v in g[u]:
                go(v)

            postorder.append(u)

        go(u0)

        return list(reversed(postorder))

    def get_dp(u0):
        topoorder = get_topoorder(u0)

        dp1 = {u0: 1}  # all paths
        dp2 = {u0: 1 if u0 == "fft" else 0}  # through fft
        dp3 = {u0: 1 if u0 == "dac" else 0}  # through dac
        dp4 = {u0: 0}  # through both

        for u in topoorder[1:]:
            dp1[u] = 0
            dp2[u] = 0
            dp3[u] = 0
            dp4[u] = 0

            for v in reverse_g[u]:
                if v not in dp1:
                    continue

                dp1[u] += dp1[v]
                dp2[u] += dp2[v]
                dp3[u] += dp3[v]
                dp4[u] += dp4[v]

            if u == "fft":
                dp2[u] = dp1[u]
                dp4[u] = dp3[u]

            elif u == "dac":
                dp3[u] = dp1[u]
                dp4[u] = dp2[u]

        return dp4

    dp = get_dp("svr")
    return dp["out"]


input = parse(sys.stdin.read())
print(solve1(input))
print(solve2(input))
