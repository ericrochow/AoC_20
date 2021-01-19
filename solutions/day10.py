#!/usr/bin/env python3

from utils import read_input


TEST_INPUT = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

TEST_INPUT_2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


def sort_adapters(adapters: list[int]) -> tuple[list[int]]:
    """"""
    ones, twos, threes = [], [], []
    current_joltage = 0
    for adapter in adapters:
        if adapter == current_joltage + 1:
            current_joltage = adapter
            ones.append(adapter)
        elif adapter == current_joltage + 2:
            current_joltage = adapter
            twos.append(adapter)
        elif adapter == current_joltage + 3:
            current_joltage = adapter
            threes.append(adapter)
    # account for the device itself
    threes.append(adapters[-1] + 3)
    return ones, twos, threes


def count_permutations(adapters: list[int]) -> int:
    """"""
    placeholders = [1] + [0 for x in range(len(adapters) - 1)]
    for adapter_index in range(len(adapters)):
        for next_diff in range(1, 4):
            next_val = adapters[adapter_index] + next_diff
            if next_val in adapters:
                placeholders[adapters.index(next_val)] += placeholders[adapter_index]
    return placeholders.pop()


def part_one(adapters: list) -> int:
    adapters.sort()
    ones, _, threes = sort_adapters(adapters)
    return len(ones) * len(threes)


def part_two(adapters: list) -> int:
    # account for the port itself
    adapters += [0]
    adapters.sort()
    return count_permutations(adapters)


if __name__ == "__main__":
    INPUT = [int(x) for x in read_input(10)]
    print(part_one(INPUT))
    print(part_two(INPUT))
