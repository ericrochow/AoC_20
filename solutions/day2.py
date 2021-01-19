#!/usr/bin/env python3

from utils import read_input, read_template


def part_one(parsed_input):
    count = 0
    for entry in parsed_input:
        occurances = entry[3].count(entry[2])
        if int(entry[0]) <= occurances <= int(entry[1]):
            count += 1
    return count


def part_two(parsed_input):
    count = 0

    for entry in parsed_input:
        # zero-indexify
        a_position = int(entry[0]) - 1
        b_position = int(entry[1]) - 1
        # XOR positional matches
        if (entry[3][a_position] == entry[2]) ^ (entry[3][b_position] == entry[2]):
            count += 1
    return count


if __name__ == "__main__":
    TEMPLATE = read_template(2)
    PARSED_INPUT = [TEMPLATE.ParseText(x) for x in read_input(2)].pop()

    print(part_one(PARSED_INPUT))
    print(part_two(PARSED_INPUT))
