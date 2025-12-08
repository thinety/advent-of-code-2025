from math import prod
import sys
from typing import Literal


type Input = tuple[list[list[str]], list[Literal["+", "*"]]]


def parse(input: str) -> Input:
    def assert_literal(c):
        assert c == "+" or c == "*"
        return c

    lines = input.strip().split("\n")

    operands = []
    operations = []

    last_i = 0
    for i in range(1, len(lines[-1])):
        if lines[-1][i] == " ":
            continue
        operations.append(assert_literal(lines[-1][last_i]))
        operands.append([line[last_i : i - 1] for line in lines[:-1]])
        last_i = i
    operations.append(assert_literal(lines[-1][last_i]))
    operands.append([line[last_i:] for line in lines[:-1]])

    return operands, operations


def solve1(input: Input):
    operands, operations = input

    ans = 0
    for nums, op in zip(operands, operations):
        nums = (int(x) for x in nums)
        match op:
            case "+":
                ans += sum(nums)
            case "*":
                ans += prod(nums)

    return ans


def solve2(input: Input):
    operands, operations = input

    ans = 0
    for nums, op in zip(operands, operations):
        nums = [
            int("".join(nums[i][j] for i in range(len(nums))))
            for j in range(len(nums[0]))
        ]
        match op:
            case "+":
                ans += sum(nums)
            case "*":
                ans += prod(nums)

    return ans


input = parse(sys.stdin.read())
print(solve1(input))
print(solve2(input))
