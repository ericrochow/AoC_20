#!/usr/bin/env python3

from collections import deque

import ipdb  # noqa: F401

from tqdm import tqdm

TEST_INPUT = "389125467"


def find_destination(cups: deque, current_cup: int) -> int:
    """"""
    destination = current_cup - 1
    while destination not in cups and destination >= min(cups):
        destination -= 1
    return destination if destination >= min(cups) else max(cups)


def simulate_turn(cups: deque) -> deque:
    """"""
    current_cup = cups.popleft()
    picked_up = [cups.popleft(), cups.popleft(), cups.popleft()]
    next_cup = cups[0]
    destination = find_destination(cups, current_cup)
    # while cups[0] != destination:
    while cups[-1] != destination:
        cups.rotate(-1)
    # cups.rotate(-1)
    for p in picked_up:
        cups.append(p)
    while cups[0] != next_cup:
        cups.rotate(-1)
    cups.append(current_cup)
    # ipdb.set_trace()
    return cups


def simulate_game(cups: deque, rounds: int) -> deque:
    """"""
    for _ in tqdm(range(rounds)):
        cups = simulate_turn(cups)
    return find_end_order(cups)


def find_end_order(cups: deque) -> str:
    while cups[0] != 1:
        cups.rotate(-1)
    cups.popleft()
    return "".join([str(x) for x in cups])


def part_one(cup_input: deque):
    return simulate_game(cup_input, 100)


def part_two(cup_input: deque):
    for num in range(10, 1000001):
        cup_input.append(num)
    return simulate_game(cup_input, 10000000)


if __name__ == "__main__":
    INPUT = "326519478"
    # INPUT = TEST_INPUT
    cups = deque([int(x) for x in INPUT])
    print(part_one(cups))
    print(part_two(cups))
