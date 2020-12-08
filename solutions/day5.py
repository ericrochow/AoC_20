#!/usr/bin/env python3

from utils import read_input


def sort_seat_chart(seat_chart):
    sorted_seat_chart = sorted([seat_id(seat) for seat in seat_chart])
    return sorted_seat_chart


def binary_string_to_int(binary_string):
    binary_tuple = tuple(binary_string[i] for i in range(0, len(binary_string)))
    r = int("".join(str(i) for i in binary_tuple), 2)
    return r


def seat_id(position):
    binary_string = (
        position.replace("F", "0")
        .replace("L", "0")
        .replace("B", "1")
        .replace("R", "1")
    )
    seat_id = binary_string_to_int(binary_string)
    return seat_id


def part_one(seat_chart):
    highest_id = sort_seat_chart(seat_chart).pop()
    print(highest_id)


def part_two(seat_chart):
    seat_ids = sort_seat_chart(seat_chart)
    last_id = seat_ids[0]
    print(last_id)
    for seat in seat_ids[1:]:
        if seat != last_id + 1:
            print(seat - 1)
            break
        last_id = seat


if __name__ == "__main__":
    INPUT = read_input(5)
    print(part_one(INPUT))
    print(part_two(INPUT))
