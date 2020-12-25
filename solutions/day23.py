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


class Cup:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class CupRing:
    def __init__(self, cups: list = None, maximum: int = None):
        self.head = None
        self.lowest_cup = "1"
        if maximum:
            for num in range(len(cups), maximum + 1):
                cups.append(str(num))
        self.highest_cup = str(max(list(map(int, cups))))
        if cups is not None:
            cup = Cup(data=cups.pop(0))
            self.head = cup
            for c in cups:
                cup.next = Cup(data=c)
                cup = cup.next

    def __repr__(self):
        cup = self.head
        cups = []
        while cup is not None:
            cups.append(cup.data)
            cup = cup.next
        return " -> ".join(cups)

    def __next__(self):
        cup = self.head
        cup = cup.next
        return cup

    def push(self, cup):
        cup.next = self.head
        self.head = cup

    def append(self, cup):
        if not self.head:
            self.head = cup
            return
        for current_cup in self:
            pass
        current_cup.next = cup

    def instert_after(self, target_cup_data, new_cup):
        if not self.head:
            raise Exception("No cups!")

        for cup in self:
            if cup.data == target_cup_data:
                new_cup.next = cup.next
                cup.next = new_cup
                return

        raise Exception(f"Node with data {target_cup_data} not found!")

    def insert_before(self, target_cup_data, new_cup):
        if not self.head:
            raise Exception("No cups!")

        if self.head.data == target_cup_data:
            return self.push(new_cup)

        prev_cup = self.head
        for cup in self:
            if cup.data == target_cup_data:
                prev_cup.next = new_cup
                new_cup.next = cup
                return
            prev_cup = cup

        raise Exception(f"Node with {target_cup_data} not found.")

    def remove_cup(self, target_cup_data):
        if not self.head:
            raise Exception("No cups!")

        if self.head.data == target_cup_data:
            self.head = self.head.next
            return

        prev_cup = self.head
        for cup in self:
            if cup.data == target_cup_data:
                prev_cup.next = cup.next
                return
            prev_cup = cup
        raise Exception(f"Node with data {target_cup_data} not found.")

    def traverse_cups(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        cup = starting_point
        while cup is not None and cup.next != starting_point:
            yield cup
            cup = cup.next
        yield cup

    def print_cup_list(self, starting_point=None):
        cups = []
        for cup in self.traverse_cups(starting_point):
            cups.append(str(cup))
        print(" -> ".join(cups))

    def simulate_round(self):
        tail = self.head
        removed = deque()
        for _ in range(3):
            removed.append(tail)
            tail = cup_ring[tail]
        # connect the current cup to the tail, removing the 3 cups between
        cup_ring[cup_ring[0]] = tail
        # select destination cup
        destination = cup_ring[0]
        while True:
            destination -= 1
            if destination < self.lowest_cup:
                destination = self.highest_cup
            if destination not in removed:
                break
        # insert removed cups clockwise of dest
        # connect the last removed cup to the cup after dest
        cup_ring[removed[-1]] = cup_ring[destination]
        # connect dest to the first removed cup
        cup_ring[destination] = self.head
        # advance the current cup
        cup_ring[0] = cup_ring[cup_ring[0]]
        return cup_ring


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
    cup_ring[removed[-1]] = cup_ring[destination]
    # connect dest to the first removed cup
    cup_ring[destination] = head
    # advance the current cup
    cup_ring[0] = cup_ring[cup_ring[0]]
    return cup_ring


def part_one(cup_input: deque):
    return simulate_game(cup_input, 100)


def part_two(cups: list) -> int:
    """"""
    cups += range(max(cups) + 1, 1000001)
    cup_ring, highest_cup, lowest_cup = generate_cups_linked_list(cups)
    for _ in tqdm(range(10000000)):
        cup_ring = simulate_round(cup_ring, highest_cup, lowest_cup)
    return cup_ring[1] * cup_ring[cup_ring[1]]


if __name__ == "__main__":
    INPUT = "326519478"
    # INPUT = TEST_INPUT
    # cups = deque([int(x) for x in INPUT])
    cups = list(INPUT)
    cup_ring = CupRing(cups)
    ipdb.set_trace()
    # print(part_one(cups))
    cups = list(map(int, INPUT))
    # print(part_two(cups))
