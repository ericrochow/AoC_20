#!/usr/bin/env python3

from collections import deque

import ipdb  # noqa: F401

from tqdm import tqdm

TEST_INPUT = "389125467"


def generate_cups_linked_list(cups: list) -> tuple:
    """
    Generates a linked list simulating the cup ring.

    Args:
        cups: A list contining the initial order of all cups
    Returns:
        A tuple containing the linked list of cups (i.e. the ring), the highest cup,
            and the lowest cup.
    """
    cup_ring = [None] * (len(cups) + 1)
    highest_cup = len(cups)
    lowest_cup = 1
    cup_ring[0] = cups[0]
    for current_cup, next_cup in zip(cups, cups[1:]):
        cup_ring[current_cup] = next_cup
    cup_ring[next_cup] = cup_ring[0]
    return cup_ring, highest_cup, lowest_cup


def simulate_round(cup_ring: list, highest_cup: int, lowest_cup: int) -> list:
    """
    Simulates a round of the cup game.

    Args:
        cup_ring: A linked list contianing the current order of cups
        highest_cup: The current highest cup
        lowest_cup: The current lowest cup
    Returns:
        A list containing the updated cup ring.
    """
    # find the first cup we need to remove, which is the cup after current
    head = cup_ring[cup_ring[0]]
    # move 3 cups ahead of head to find the tail, the first unremoved cup
    # at the same time, take note of what we removed
    tail = head
    removed = deque()
    for _ in range(3):
        removed.append(tail)
        tail = cup_ring[tail]
        # ipdb.set_trace()
    # connect the current cup to the tail, removing the 3 cups between
    cup_ring[cup_ring[0]] = tail
    # select destination cup
    destination = cup_ring[0]
    while True:
        destination -= 1
        if destination < lowest_cup:
            destination = highest_cup
        if destination not in removed:
            break
    # insert removed cups clockwise of dest
    # connect the last removed cup to the cup after dest
    # ipdb.set_trace()
    cup_ring[removed[-1]] = cup_ring[destination]
    # ipdb.set_trace()
    # connect dest to the first removed cup
    cup_ring[destination] = head
    # advance the current cup
    cup_ring[0] = cup_ring[cup_ring[0]]
    return cup_ring


def part_two(cups: list) -> int:
    """"""
    # ipdb.set_trace()
    cups += range(max(cups) + 1, 1000001)
    cup_ring, highest_cup, lowest_cup = generate_cups_linked_list(cups)
    for _ in tqdm(range(10000000)):
        cup_ring = simulate_round(cup_ring, highest_cup, lowest_cup)
    return cup_ring[1] * cup_ring[cup_ring[1]]


if __name__ == "__main__":
    INPUT = "326519478"
    # INPUT = TEST_INPUT
    cups = list(map(int, INPUT))
    # print(part_one(cups))
    print(part_two(cups))
