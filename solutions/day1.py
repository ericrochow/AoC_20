#!/usr/bin/env python3

from utils import read_input


def part_one(vals):
    for x in vals:
        for y in vals:
            if int(x) + int(y) == 2020:
                return int(x) * int(y)


def part_two(vals):
    for x in vals:
        for y in vals:
            for z in vals:
                if int(x) + int(y) + int(z) == 2020:
                    return int(x) * int(y) * int(z)


if __name__ == "__main__":
    INPUT = read_input(1)
    print(part_one(INPUT))
    print(part_two(INPUT))
