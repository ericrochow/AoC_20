#!/usr/bin/env python3

# import pytest

from solutions import day13

TEST_INPUT_1 = ["939", "7,13,x,x,59,x,31,19"]  # == 1068788
TEST_INPUT_2 = ["100", "17,x,13,19"]  # == 3417
TEST_INPUT_3 = ["100", "67,7,59,61"]  # == 754018
TEST_INPUT_4 = ["100", "67,x,7,59,61"]  # == 779210
TEST_INPUT_5 = ["100", "67,7,x,59,61"]  # == 1261476
TEST_INPUT_6 = ["100", "1789,37,47,1889"]  # == 1202161486
TEST_INPUT_7 = ["100", "x,7,x,5,x,x,8"]  # == 78
TEST_INPUT_8 = ["100", "x,x,6,5,7"]  # == 23
TEST_INPUT_9 = ["100", "x,2,3,5,7"]  # == 53


def test__prod():
    assert day13._prod([9, 10]) == 90
