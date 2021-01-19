#!/usr/bin/env python3

import re

from utils import read_input, read_template

TEST_INPUT = [
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
]


TEST_INPUT_2 = [""]


def find_valid_ranges(ticket_info: list) -> list:
    valid_ranges = []
    for line in ticket_info:
        valid_ranges += re.findall(r"\d+-\d+", line)
    return valid_ranges


def ranges_to_numbers(valid_ranges: list) -> set:
    valid_numbers = set()
    for valid_range in valid_ranges:
        results = re.findall(r"\d+", valid_range)
        if results:
            low, high = int(results[0]), int(results[1]) + 1
            valid_numbers.update(range(low, high))
    return valid_numbers


def define_nearby_tickets(ticket_info: list) -> list:
    nearby = []
    nearby_found = False
    for line in ticket_info:
        if nearby_found:
            line = [int(num) for num in line.split(",")]
            nearby.append(line)
        elif "nearby" in line:
            nearby_found = True
    return nearby


def define_my_ticket(ticket_info: list) -> list:
    for index, line in enumerate(ticket_info):
        if "your ticket" in line:
            my_ticket = ticket_info[index + 1]
            continue
    return [int(x) for x in my_ticket.split(",")]


def find_invalid_numbers(valid_numbers: set, nearby_tickets: list) -> list:
    return [
        # num for num for ticket in nearby_tickets if num not in valid_numbers
        num
        for ticket in nearby_tickets
        for num in ticket
        if num not in valid_numbers
    ]


def define_ticket_rules(parsed_rules: list) -> dict:
    rules = {}
    for rule in parsed_rules:
        rules[rule[0]] = [rule[1], rule[2]]
    return rules


def remove_invalid_tickets(tickets: list, valid_numbers: set) -> list:
    valid_tickets = []
    for ticket in tickets:
        skip = False
        for value in ticket:
            if value not in valid_numbers:
                skip = True
                break
        if not skip:
            valid_tickets.append(ticket)
    return valid_tickets


def detect_rule_order_possibilities(tickets: list, rules: dict) -> dict:
    rule_order = {}
    for col in range(0, len(tickets[0])):
        col_vals = set()
        for ticket in tickets:
            col_vals.add(ticket[col])
        possible = []
        for name, rule in rules.items():
            if col_vals.intersection(rule) == col_vals:
                possible.append(name)
        if possible:
            rule_order[col] = possible
    return rule_order


def deduplicate_order_possibilities(possibilities: dict) -> dict:
    """
    Iterates over each k, v pair until it finds one with a single value.
    Remove that value from all k, v pairs with len(v) > 1.
    Loop until all all v are len 1
    Return dict
    """
    deduped = []
    while len(deduped) < len(possibilities):
        for k, v in possibilities.items():
            if len(v) == 1 and v[0] not in deduped:
                dedup = v[0]
                continue
        for k, v in possibilities.items():
            if len(v) > 1:
                try:
                    possibilities[k].remove(dedup)
                except ValueError:
                    pass
        deduped.append(dedup)
    return possibilities


def find_departure_keys(rule_order: dict) -> list:
    keys = []
    for k, v in rule_order.items():
        if v[0].startswith("departure"):
            keys.append(k)
    return keys


def multiply_all_values(keys: list, my_ticket: list) -> int:
    total = 1
    for key in keys:
        total *= my_ticket[key]
    return total


def part_one(ticket_info):
    valid_ranges = find_valid_ranges(ticket_info)
    nearby_tickets = define_nearby_tickets(ticket_info)
    valid_numbers = ranges_to_numbers(valid_ranges)
    invalid_numbers = find_invalid_numbers(valid_numbers, nearby_tickets)
    return sum(invalid_numbers)


def part_two(ticket_info: list, parsed_rules: list):
    rules = define_ticket_rules(parsed_rules)
    for rule_name, rule_value in rules.items():
        rules[rule_name] = ranges_to_numbers(rule_value)
    valid_numbers = set.union(*rules.values())
    my_ticket = define_my_ticket(ticket_info)
    nearby_tickets = define_nearby_tickets(ticket_info)
    valid_tickets = remove_invalid_tickets(nearby_tickets, valid_numbers)
    possibilities = detect_rule_order_possibilities(valid_tickets, rules)
    rule_order = deduplicate_order_possibilities(possibilities)
    keys = find_departure_keys(rule_order)
    return multiply_all_values(keys, my_ticket)


if __name__ == "__main__":
    TEMPLATE = read_template(16)
    INPUT = read_input(16)
    PARSED_RULES = [TEMPLATE.ParseText(x) for x in INPUT].pop()
    print(part_one(INPUT))
    print(part_two(INPUT, PARSED_RULES))
