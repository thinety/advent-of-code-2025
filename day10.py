import sys
import z3


type Input = list[tuple[list[bool], list[list[int]], list[int]]]


def parse(input: str) -> Input:
    def parse_machine(input):
        items = input.split()

        lights = items[0]
        buttons = items[1:-1]
        joltages = items[-1]

        lights = [True if light == "#" else False for light in lights[1:-1]]
        buttons = [list(map(int, button[1:-1].split(","))) for button in buttons]
        joltages = list(map(int, joltages[1:-1].split(",")))

        return lights, buttons, joltages

    return [parse_machine(line) for line in input.strip().split("\n")]


# def solve1(input: Input):
#    ans = 0
#
#    for machine in input:
#        lights, buttons, _ = machine
#
#        lights = sum(2**i for i, light in enumerate(lights) if light)
#        buttons = [sum(2**i for i in button) for button in buttons]
#
#        machine_ans = float("inf")
#
#        n = len(buttons)
#        for mask in range(2**n):
#            result = 0
#            count = 0
#            for i in range(n):
#                if (mask & (1 << i)) != 0:
#                    result ^= buttons[i]
#                    count += 1
#            if result == lights:
#                machine_ans = min(machine_ans, count)
#
#        ans += machine_ans
#
#    return ans


def solve1(input: Input):
    ans = 0

    for machine in input:
        lights, buttons, _ = machine

        n = len(buttons)

        button_mask = [[False for _ in lights] for _ in range(n)]
        for button, mask in zip(buttons, button_mask):
            for i in button:
                mask[i] = True

        button_press = [z3.Int(f"p_{i}") for i in range(n)]

        solver = z3.Optimize()

        solver.add([p >= 0 for p in button_press])
        solver.add(
            [
                z3.Sum(button_press[i] for i in range(n) if button_mask[i][l]) % 2
                == (1 if light else 0)
                for l, light in enumerate(lights)
            ]
        )
        solver.minimize(z3.Sum(button_press))

        solver.check()
        model = solver.model()

        ans += sum(model[p].as_long() for p in button_press)

    return ans


def solve2(input: Input):
    ans = 0

    for machine in input:
        _, buttons, joltages = machine

        n = len(buttons)

        button_mask = [[False for _ in joltages] for _ in range(n)]
        for button, mask in zip(buttons, button_mask):
            for i in button:
                mask[i] = True

        button_press = [z3.Int(f"p_{i}") for i in range(n)]

        solver = z3.Optimize()

        solver.add([p >= 0 for p in button_press])
        solver.add(
            [
                z3.Sum(button_press[i] for i in range(n) if button_mask[i][j])
                == joltage
                for j, joltage in enumerate(joltages)
            ]
        )
        solver.minimize(z3.Sum(button_press))

        solver.check()
        model = solver.model()

        ans += sum(model[p].as_long() for p in button_press)

    return ans


input = parse(sys.stdin.read())
print(solve1(input))
print(solve2(input))
