#!/usr/bin/env python3

import ipdb  # noqa: F401

from utils import read_input

TEST_INPUT_1 = ["939", "7,13,x,x,59,x,31,19"]  # == 1068788
TEST_INPUT_2 = ["100", "17,x,13,19"]  # == 3417
TEST_INPUT_3 = ["100", "67,7,59,61"]  # == 754018
TEST_INPUT_4 = ["100", "67,x,7,59,61"]  # == 779210
TEST_INPUT_5 = ["100", "67,7,x,59,61"]  # == 1261476
TEST_INPUT_6 = ["100", "1789,37,47,1889"]  # == 1202161486
TEST_INPUT_7 = ["100", "x,7,x,5,x,x,8"]  # == 78
TEST_INPUT_8 = ["100", "x,x,6,5,7"]  # == 23
TEST_INPUT_9 = ["100", "x,2,3,5,7"]  # == 53


def _prod(number_list: list) -> int:
    """
    Returns the product of all values in a list.
    """
    value = 1
    for num in number_list:
        value *= num
    return value


def enumerate_busses(bus_list: list) -> list:
    """"""
    return [
        (index, int(value)) for index, value in enumerate(bus_list) if value != "x"
    ]


def resolve_x_i(N_i: int, n_i: int) -> int:
    """
    Resolves x_i for the Chinese remainder theorem.

    The variables in this function follow the congruency statement that

    N_i * x_i ≅ b_i % N_i

    First we reduce N_i to the smallest valid value using the modulus operator.
    Following this, we perform trial and error until we find a value for x_i that

    N_i * x_i == 1 % n_i.

    Args:
        N_i: An integer specifying the factor of x_i
        n_i: An integer specifying the modulus in the statement.
    Returns:
        An integer specifying the value of x_i.
    """
    N_i = N_i % n_i
    x_i = 0
    while True:
        x_i += 1
        # N_i * x_i = 1 mod n_i
        if (N_i * x_i) % n_i == 1 % n_i:
            return x_i
    return x_i


def chinese_remainder_by_hand(bus_list: list) -> int:
    """
    Finds the Chinese Remainder for the given dataset.

    We are given the n_i and b_i values for each bus, so we need to figure out N as
    well as each N_i value, then use those three values to determine our x_i values.
    The answer is then the sum of the product of b_i, N_i, and x_i for each each
    congruence statement.

    Args:
        bus_list: An enumerated list of busses minus the out-of-service busses
    Returns:
        An integer specifying the Chinese Remainder of the given busses.
    """
    b_list = [(r[1] - r[0]) % r[1] for r in bus_list]
    n_list = [n[1] for n in bus_list]
    N = _prod(n_list)
    N_list = [N // n for n in n_list]
    x_list = [resolve_x_i(*z) for z in zip(N_list, n_list)]
    c_remainder = 0
    for i in range(len(N_list)):
        c_remainder += b_list[i] * N_list[i] * x_list[i]
    return c_remainder % N


def part_one(earliest, bus_list):
    soonest_runs = {}
    busses = [int(bus) for bus in bus_list if bus != "x"]
    for bus in busses:
        bus_start = bus
        while bus_start < earliest:
            bus_start += bus
        soonest_runs[bus] = bus_start
    soonest_depart = min(soonest_runs.values())
    bus_id = [key for key in soonest_runs if soonest_runs[key] == soonest_depart][0]
    minutes_to_wait = soonest_depart - earliest
    return bus_id * minutes_to_wait


def part_two(bus_list: list) -> int:
    """"""
    bus_list = enumerate_busses(bus_list)
    return chinese_remainder_by_hand(bus_list)


if __name__ == "__main__":
    INPUT = read_input(13)
    # INPUT = TEST_INPUT_5
    EARLIEST = int(INPUT[0])
    BUS_LIST = [x for x in INPUT[1].split(",")]
    print(part_one(EARLIEST, BUS_LIST))
    print(part_two(BUS_LIST))
