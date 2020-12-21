#!/usr/bin/env python3


import ipdb  # noqa: F401
import re

from utils import read_input


TEST_INPUT_1 = [
    "0: 1 2",
    '1: "a"',
    "2: 1 3 | 3 1",
    '3: "b"',
]
TEST_INPUT_2 = [
    "0: 4 1 5",
    "1: 2 3 | 3 2",
    "2: 4 4 | 5 5",
    "3: 4 5 | 5 4",
    '4: "a"',
    '5: "b"',
    "",
    "ababbb",
    "bababa",
    "abbbab",
    "aaabbb",
    "aaaabbb",
]


def generate_rules(file_input: list) -> dict:
    rule_db = {}
    for line in file_input:
        line = line.split()
        if not line:
            continue
        elif line[0].endswith(":"):
            rule_no = line[0].strip(":")
            try:
                rule = " ".join(line[1:]).strip('"')
                rule = rule.split()
            except IndexError:
                break
        rule_db[rule_no] = rule
    return rule_db


def generate_messages(file_input: list) -> list:
    """"""
    messages = []
    for line in file_input:
        if len(line.split()) == 1:
            messages.append(line)
    return messages


def generate_matching_groups(rule: list) -> list:
    if "|" in rule and rule[0] != "(":
        rule = ["("] + rule + [")"]
    return rule


def resolve_rule_references(rule_db: dict, max_passes=1000) -> dict:
    solved = []
    passes = 0
    while len(solved) < len(rule_db) and passes < max_passes:
        for key, value in rule_db.items():
            for index, item in enumerate(value):
                if (
                    not any(re.match(r"\d+", item) for item in rule_db[key])
                    and key not in solved
                ):
                    solved.append(key)
        for key, value in rule_db.items():
            rule = generate_matching_groups(value)
            for index, item in enumerate(value):
                for s in solved:
                    if item == s:
                        rule = generate_matching_groups(rule_db[s])
                        rule_db[key][index] = "".join(rule)
        passes += 1
    return rule_db


def generate_regex_values(rule_db: dict) -> dict:
    for key, value in rule_db.items():
        rule_db[key] = "^" + "".join(value) + "$"
    return rule_db


def count_matches(rule_db: dict, messages: list, key: str) -> int:
    """"""
    count = 0
    for m in messages:
        if re.match(rule_db[key], m):
            count += 1
    return count


def part_one(file_input: list):
    rule_db = generate_rules(file_input)
    messages = generate_messages(file_input)
    rule_db = resolve_rule_references(rule_db)
    rule_db = generate_regex_values(rule_db)
    count = count_matches(rule_db, messages, "0")
    return count


def part_two(file_input: list):
    rule_db = generate_rules(file_input)
    messages = generate_messages(file_input)
    rule_db = resolve_rule_references(rule_db)
    rule_db = generate_regex_values(rule_db)
    count = count_matches(rule_db, messages, "0")
    return count


if __name__ == "__main__":
    PART_ONE_INPUT = read_input("19_part1")
    PART_TWO_INPUT = read_input("19_part2")
    print(part_one(PART_ONE_INPUT))
    print(part_two(PART_TWO_INPUT))
