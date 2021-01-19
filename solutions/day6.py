#!/usr/bin/env python3

from utils import read_input


def unique_answers(answers):
    answers = answers.replace("\n", "")
    unique = set(answers)
    return len(unique)


def group_overlap(answers):
    answers = answers.split("\n")
    group_yeses = answers[0]
    for person in answers:
        if person:
            group_yeses = set(group_yeses) & set(person)
    return len(group_yeses)


def part_one(answers):
    group_answers = [unique_answers(group) for group in answers]
    total_yeses = sum(group_answers)
    return total_yeses


def part_two(answers):
    group_answers = [group_overlap(group) for group in answers if group]
    total_yeses = sum(group_answers)
    return total_yeses


if __name__ == "__main__":
    INPUT = read_input(6, output="blob")
    ANSWERS = INPUT.split("\n\n")
    print(part_one(ANSWERS))
    print(part_two(ANSWERS))
