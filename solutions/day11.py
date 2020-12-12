#!/usr/bin/env python3


from itertools import product
from copy import deepcopy

from utils import read_input

TEST_INPUT = (
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
)


def define_cardinalities() -> list[tuple]:
    """"""
    cardinalities = list(product(range(-1, 2), range(-1, 2)))
    cardinalities.remove((0, 0))
    return cardinalities


def define_adjacencies(coords: tuple[int]) -> list[tuple]:
    """
    Creates a list of all valid coordinates surrounding the given coordinates.

    Args:
      coords: A tuple of integers specifying the coordinates (row, column) of the seat
          whose adjacencies to define
    Returns:
      A list of tuples containing valid coordinates.
    """
    adjacencies = []
    adj_offsets = product(range(-1, 2), range(-1, 2))
    # adj_offsets = define_cardinalities()
    for x, y in adj_offsets:
        if x == 0 and y == 0:
            continue
        r = coords[0] + x
        c = coords[1] + y
        if r >= 0 and c >= 0:
            adjacencies.append((r, c))
    return adjacencies


def define_visible(coords: tuple[int], maxes: tuple[int]) -> list[tuple]:
    """
    Creates a list of all valid coordinates of visible coordinates.

    Visible is defined as a straight line vertically, horizontally, or diagonally.

    Args:
      coords: A tuple of integers specifying the coordinates (row, column) of the seat
          whose lines of site to define
      maxes: A tuple of integers specifying the upper bounds of the coordinates
    Returns:
      A list of tuples containing valid coordinates.
    """
    visible = []
    right_bound = maxes[0]
    bottom_bound = maxes[1]
    current_row, current_col = coords
    for card in define_cardinalities():
        path = []
        while current_row >= 0 and current_col >= 0:
            current_row += card[0]
            current_col += card[1]
            if (
                current_row >= 0
                and current_row < bottom_bound + 2
                and current_col >= 0
                and current_col < right_bound + 2
            ):
                path.append((current_row, current_col))
            else:
                break
                # print("woopsie")
        current_row, current_col = coords
        if len(path) > 0:
            visible.append(path)
    return visible


def count_occupied_adjacent(adjacencies: list[tuple], seat_chart: list[list]) -> int:
    """
    Counts the number of occupied adjacent seats.

    Args:
      adjacencies: A list of tuples specifying the adjacent seats to check for
          occupancy
      seat_chart: A list of lists specifying the current seating chart
    Returns:
      An integer specifying the number of adjacent seats that are occupied.
    """
    occupied = 0
    for adj in adjacencies:
        try:
            seat = seat_chart[adj[0]][adj[1]]
            if seat == "#":
                occupied += 1
        except IndexError:
            pass
    return occupied


def count_occupied_visible(visible: list[tuple], seat_chart: list[list]) -> int:
    """
    Counts the number of occupied adjacent seats.

    Args:
      adjacencies: A list of tuples specifying the adjacent seats to check for
          occupancy
      seat_chart: A list of lists specifying the current seating chart
    Returns:
      An integer specifying the number of adjacent seats that are occupied.
    """
    occupied = 0
    for path in visible:
        for coord in path:
            try:
                if seat_chart[coord[0]][coord[1]] == "#":
                    occupied += 1
                    break
                elif seat_chart[coord[0]][coord[1]] == "L":
                    break
            except IndexError:
                break
    return occupied


def simulate_seat_change_p1(before: list[list], tolerance: int) -> list[list]:
    """
    Simulates all seating changes per pass per the provided rules.

    Args:
      before: A list of lists specifying the seating chart prior to the round of
          changes
      tolerance: An integer specifying the number of occupied adjacent seats people
          will tolerate prior to vacating their seat
    Returns:
      A list of lists specifying the seating chart at the end of the round of changes.
    """
    after = deepcopy(before)
    for rindex, row in enumerate(before):
        for sindex, seat in enumerate(row):
            adjacencies = define_adjacencies((rindex, sindex))
            occupied = count_occupied_adjacent(adjacencies, before)
            if seat == "L" and occupied == 0:
                after[rindex][sindex] = "#"
            elif seat == "#" and occupied <= tolerance:
                after[rindex][sindex] = "L"
    return after


def simulate_seat_change_p2(before: list[list], tolerance: int) -> list[list]:
    """
    Simulates all seating changes per pass per the provided rules.

    Args:
      before: A list of lists specifying the seating chart prior to the round of
          changes
      tolerance: An integer specifying the number of occupied adjacent seats people
          will tolerate prior to vacating their seat
    Returns:
      A list of lists specifying the seating chart at the end of the round of changes.
    """
    after = deepcopy(before)
    maxes = (len(before), len(before[0]))
    for rindex, row in enumerate(before):
        for sindex, seat in enumerate(row):
            visible = define_visible((rindex, sindex), maxes)
            occupied = count_occupied_visible(visible, before)
            if seat == "L" and occupied == 0:
                after[rindex][sindex] = "#"
            elif seat == "#" and occupied >= tolerance:
                after[rindex][sindex] = "L"
    # import ipdb

    # ipdb.set_trace()
    return after


def part_one(seat_chart: list) -> int:
    before = [list(row) for row in seat_chart]
    while True:
        after = simulate_seat_change_p1(before, 4)
        if after == before:
            total_occupied = 0
            for row in after:
                total_occupied += row.count("#")
            return total_occupied
        before = deepcopy(after)


def part_two(seat_chart):
    before = [list(row) for row in seat_chart]
    while True:
        after = simulate_seat_change_p2(before, 5)
        if after == before:
            print("\n".join(["".join(row) for row in after]))
            total_occupied = 0
            for row in after:
                total_occupied += row.count("#")

            return total_occupied
        before = deepcopy(after)


if __name__ == "__main__":
    INPUT = read_input(11)
    # INPUT = TEST_INPUT
    # print(part_one(INPUT))
    print(part_two(INPUT))
