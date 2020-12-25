#!/usr/bin/env python3

from collections import Counter
import ipdb  # noqa:F401

from utils import read_input


TEST_INPUT = [
    "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
    "trh fvjkl sbzzf mxmxvkd (contains dairy)",
    "sqjhc fvjkl (contains soy)",
    "sqjhc mxmxvkd sbzzf (contains fish)",
]


def create_lists(file_input: list) -> tuple:
    """"""
    ingreds, allergens = [], []
    for i in file_input:
        row = i.split("(contains ")
        ingreds += row[0].split()
        allergens += row[1].strip(")").split()
    return ingreds, allergens


def create_counter(ingreds: list) -> Counter:
    """"""
    return Counter(ingreds)


def part_one(file_input: list) -> int:
    ingreds, allergens = create_lists(file_input)
    ingred_counter = create_counter(ingreds)
    ipdb.set_trace()


def part_two(file_input: list) -> int:
    pass


if __name__ == "__main__":
    INPUT = read_input(21)
    # INPUT = TEST_INPUT
    print(part_one(INPUT))
    print(part_two(INPUT))
