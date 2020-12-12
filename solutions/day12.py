#!/usr/bin/env python3

from utils import read_input

TEST_INPUT = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]


def part_one(instructions):
    east, north = 0, 0
    directions = {"E": 1, "S": -1, "W": -1, "N": 1}
    turns = {"L": -1, "R": 1}
    direction = 0
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "F":
            action = list(directions)[direction]
        if action == "N" or action == "S":
            north += directions[action] * value
        elif action == "E" or action == "W":
            east += directions[action] * value
        elif action == "L" or action == "R":
            value = int(value / 90)
            direction = (direction + (turns[action] * value)) % 4
    return abs(north) + abs(east)


def part_two(instructions):
    waypoint = (10, 1)
    pass


if __name__ == "__main__":
    INPUT = read_input(12)
    INPUT = TEST_INPUT
    print(part_one(INPUT))
    print(part_two(INPUT))
