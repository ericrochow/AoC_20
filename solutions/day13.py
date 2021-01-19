#!/usr/bin/env python3

# from functools import reduce

# only imported due to missing import in sympy
# import sys  # noqa: F401

import ipdb  # noqa: F401

# rom sympy.ntheory.modular import crt, symmetric_residue, solve_congruence

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
# EXAMPLE_1 = [(3, 5), (1, 7), (6, 8)]  # == 78
# EXAMPLE_2 = [(3, 5), (2, 6), (4, 7)]  # == 23
# EXAMPLE_3 = [(1, 2), (2, 3), (3, 5), (4, 7)]  # == 53


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


# def find_gcd(a: int, b: int) -> int:
# """
# Applies the Extended Euclidean Algorithm to two values to determine the Greatest
# Common Divisor.
#
# Args:
# a: An integer specifying the first integer to compare
# b: An integer specifying the second integer to compare
# Returns:
# An integer specifying the greatest common demoninator of the two provided
# integers.
# """
# if a == 0 or b == 0:
# return 0
# if a == b:
# return a
# if a > b:
# return find_gcd(a - b, b)
# return find_gcd(a, b - a)


def euclidean_algorithm(a: int, b: int) -> int:
    """
    Uses the Euclidean Algorithm to determine the GCD of two numbers.

    The Euclidean algorithm determines the GCD by dividing the larger number b by the
    smaller number a and assigning that value to x and the remainder to y such that

    b = a(x) + y

    This is applied recusively by assigning b = a and a = y until y == 0. At that point
    the previous y can be assumed to be the GCD.

    Args:
        a: An integer specifying the first number to compare
        b: An integer specifying the second number to compare
    Returns:
        An integer specifying the GCD of the two numbers.
    """
    if b < a:
        a, b = b, a
    # x = b // a
    y = b % a
    while y > 0:
        old_a = a
        # old_b = b
        # old_x = x
        old_y = y
        b, a = old_a, old_y
        # x = b // a
        y = b % a
    return old_y


def extended_euclidean_algorithm(a: int, b: int) -> tuple:
    """
    Performs the extended Euclidean algorithm on the given integers a and b.

    gcd(a, b) = ax + by

    Args:
        a: An integer specifying the first integer to evaluate
        b: An integer specifying the second integer to evaluate
    Returns:
        A tuple containing the GCD and bezout coefficients.
    """
    if a == 0:
        return b, 0, 1
    gcd, temp_x, temp_y = extended_euclidean_algorithm(b % a, a)
    x = temp_y - (b // a) * temp_x
    y = temp_x
    return gcd, x, y


def find_gcd_of_list(number_list: list) -> int:
    """
    """
    a, b = number_list[0], number_list[1]
    gcd = euclidean_algorithm(a, b)
    for i in range(2, len(number_list)):
        gcd = euclidean_algorithm(gcd, number_list[i])
    return gcd


def coprime_test(a: int, b: int) -> bool:
    """
    Determines the coprimality of two integers.

    Args:
        a: An integer specifying the first integer to test
        b: An integer specifying the second integer to test
    Returns:
        A boolean specifying whether the two given integers are coprime.
    """
    return euclidean_algorithm(a, b) == 1


# def chinese_remainder(bus_list: list) -> int:
# """"""
# # remainders = [r[0] for r in bus_list]
# moduli = [m[1] for m in bus_list]
# residues = [symmetric_residue(b[0], b[1]) for b in bus_list]
# results = crt(moduli, residues, symmetric=True)
# return abs(results[0])


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
    # b_list = [r[0] for r in bus_list]
    b_list = [r[0] % r[1] for r in bus_list]
    n_list = [n[1] for n in bus_list]
    N = _prod(n_list)
    N_list = [N // n for n in n_list]
    ipdb.set_trace()
    # N_list = list(map(lambda b: int(N / b), b_list))
    # ipdb.set_trace()
    x_list = [resolve_x_i(*z) for z in zip(N_list, n_list)]
    ipdb.set_trace()
    c_remainder = 0
    for i in range(len(N_list)):
        # ipdb.set_trace()
        c_remainder += b_list[i] * N_list[i] * x_list[i]
    ipdb.set_trace()
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


def part_two_fast(bus_list: list) -> int:
    """"""
    bus_list = enumerate_busses(bus_list)
    ipdb.set_trace()
    return chinese_remainder_by_hand(bus_list)
    # return chinese_remainder(bus_list)
    # return diy_chinese_remainder(bus_list)


if __name__ == "__main__":
    INPUT = read_input(13)
    INPUT = TEST_INPUT_1
    EARLIEST = int(INPUT[0])
    BUS_LIST = [x for x in INPUT[1].split(",")]
    # print(part_one(EARLIEST, BUS_LIST))
    print(part_two_fast(BUS_LIST))
