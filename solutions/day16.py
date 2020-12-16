#!/usr/bin/env python3

import ipdb  # noqa: F401
import re

from utils import read_input

TEST_INPUT = (
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50",
    "",
    "your ticket:",
    "7,1,14",
    "",
    "nearby tickets:",
    "7,3,47",
    "40,4,50",
    "55,2,20",
    "38,6,12",
)


def find_valid_ranges(ticket_info: list) -> list:
    valid_ranges = []
    for line in ticket_info:
        valid_ranges += re.findall(r"\d+\-\d+", line)
    return valid_ranges


def ranges_to_numbers(valid_ranges: list) -> set:
    valid_numbers = set()
    for valid_range in valid_ranges:
        results = re.findall(r"\d+", valid_range)
        if results:
            low, high = int(results[0]), int(results[1]) + 1
            print(range(low, high))
            valid_numbers.update(range(low, high))
            print(valid_numbers)
    return valid_numbers


def define_nearby_tickets(ticket_info: list) -> list:
    nearby = []
    nearby_found = False
    for line in ticket_info:
        if nearby_found:
            nearby += line.split(",")
        elif "nearby" in line:
            nearby_found = True
    return nearby


def find_invalid_tickets(valid_numbers: list, nearby_tickets: list) -> list:
    return [int(ticket) for ticket in nearby_tickets if ticket not in valid_numbers]


def part_one(ticket_info):
    valid_ranges = find_valid_ranges(ticket_info)
    nearby_tickets = define_nearby_tickets(ticket_info)
    valid_numbers = ranges_to_numbers(valid_ranges)
    invalid_tickets = find_invalid_tickets(valid_numbers, nearby_tickets)
    print(invalid_tickets)
    return sum(invalid_tickets)


def part_two(ticket_info):
    pass


if __name__ == "__main__":
    INPUT = read_input(16)
    INPUT = TEST_INPUT
    print(part_one(INPUT))
    print(part_two(INPUT))
