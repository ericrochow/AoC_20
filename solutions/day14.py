#!/usr/bin/env python3

from collections import deque
from itertools import product
import re

from utils import read_input

TEST_INPUT = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0",
]

TEST_INPUT_2 = [
    "mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1",
]


def int_str_to_binary_str(value: str) -> str:
    """"""
    binary_string = bin(int(value)).lstrip("0b")
    integer_string = int(binary_string)
    return str(integer_string)


def bit_string_to_int(bit_list: list) -> int:
    """
    Convert a list of bits to an integer.

    Args:
      bit_list: A list of bits representing a binary number
    Returns:
      An integer specifying the base 10 representation of the bit list.
    """
    bit_list.reverse()
    output = 0
    for idx, bit in enumerate(bit_list):
        output += bit * 2 ** idx
    return output


def apply_bitmask_v1(value: str, mask: str) -> list:
    """"""
    value = value.zfill(36)
    value, mask = list(value), list(mask)
    for idx, val in enumerate(mask):
        if val != "X":
            value[idx] = val
    for idx, val in enumerate(value):
        value[idx] = int(val)
    return value


def apply_bitmask_v2(value: str, mask: str) -> list:
    value = value.zfill(36)
    value, mask = list(value), list(mask)
    for idx, val in enumerate(mask):
        if val != "0":
            # TODO: 1's aren't getting copied for some reason
            # print(f"Changing {value[idx]} to {val}")
            value[idx] = val
    return value


def find_floating_values(
    mask: list,
) -> list:
    floaters = mask.count("X")
    # print(mask)
    possible = deque(map(deque, product(range(2), repeat=floaters)))
    possibles = []
    while possible:
        p = possible.popleft()
        page = mask.copy()
        for i, m in enumerate(page):
            if m == "X":
                page[i] = str(p.pop())
        page = [int(x) for x in page]
        possibles.append(bit_string_to_int(page))
    return possibles


def part_one(input_code):
    memory = {}
    for line in input_code:
        if line.startswith("mask"):
            mask = line.split()[2]
        elif line.startswith("mem"):
            page, val = re.findall(r"\d+", line)
            val = int_str_to_binary_str(val)
            val = apply_bitmask_v1(val, mask)
            val = bit_string_to_int(val)
            memory[page] = val
    return sum(memory.values())


def part_two(input_code):
    memory = {}
    for line in input_code:
        if line.startswith("mask"):
            mask = line.split()[2]
        if line.startswith("mem"):
            page, val = re.findall(r"\d+", line)
            page = int_str_to_binary_str(page)
            page_mask = apply_bitmask_v2(page, mask)
            possibles = find_floating_values(page_mask)
            for p in possibles:
                memory[p] = int(val)
    return sum(memory.values())
    # return memory


if __name__ == "__main__":
    INPUT = read_input(14)
    # INPUT = TEST_INPUT_2
    print(part_one(INPUT))
    print(part_two(INPUT))
