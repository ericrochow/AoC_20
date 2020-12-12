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
    east, north = 0, 0
    waypoint = (10, 1)
    directions = {"E": 1, "S": -1, "W": -1, "N": 1}
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "F":
            east = east + (waypoint[0] * value)
            north = north + (waypoint[1] * value)
        elif action == "N" or action == "S":
            waypoint = (waypoint[0], waypoint[1] + directions[action] * value)
        elif action == "E" or action == "W":
            waypoint = (waypoint[0] + directions[action] * value, waypoint[1])
        elif action == "R":
            value = int(value / 90)
            for i in range(1, value + 1):
                # Rotate waypoint 90 deg clockwise
                waypoint = (waypoint[1], waypoint[0] * -1)
        elif action == "L" or action == "R":
            value = int(value / 90)
            for i in range(1, value + 1):
                # Rotate waypoint 90 deg counterclockwise
                waypoint = (waypoint[1] * -1, waypoint[0])
    return abs(north) + abs(east)


if __name__ == "__main__":
    INPUT = read_input(12)
    print(part_one(INPUT))
    print(part_two(INPUT))
