#!/usr/bin/env python3

import ipdb  # noqa: F401

TEST_INPUT = (5764801, 17807724)


def find_loop_size(subject: int, pub_key: int) -> int:
    """
    """
    loop_size = 0
    value = 1
    while value != pub_key:
        # print(f"{value} != {pub_key}")
        loop_size += 1
        # print(loop_size)
        value = transform(subject, value)
    return loop_size


def transform(subject: int, value: int) -> int:
    value *= subject
    value = value % 20201227
    return value


def loop_transform(subject: int, loop_size: int) -> int:
    value = 1
    for _ in range(loop_size):
        value = transform(subject, value)
    return value


def part_one(known_values: tuple) -> int:
    subject_number = 7
    door_pubkey, card_pubkey = known_values
    door_loops = find_loop_size(subject_number, door_pubkey)
    card_loops = find_loop_size(subject_number, card_pubkey)
    door_priv_key = loop_transform(card_pubkey, door_loops)
    card_priv_key = loop_transform(door_pubkey, card_loops)
    if door_priv_key == card_priv_key:
        return door_priv_key


# def part_two(known_values: tuple) -> int:
# pass


if __name__ == "__main__":
    INPUT = (14082811, 5249543)
    print(part_one(INPUT))
    # print(part_two(INPUT))
