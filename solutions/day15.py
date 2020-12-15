#!/usr/bin/env python3

import ipdb  # noqa: F401

TEST_INPUT = [0, 3, 6]
# TEST_INPUT = [1, 3, 2]
# TEST_INPUT = [2, 1, 3]
# TEST_INPUT = [1, 2, 3]
# TEST_INPUT = [2, 3, 1]


def both_parts(number_list, max_turn):
    number_map = {}
    # seed the number map
    for index, num in enumerate(number_list):
        number_map[num] = index + 1
        current_index = index + 1
    last_value = number_list[-1]
    if number_list.count(last_value) == 1:
        next_number = 0
        match_diff = False
    else:
        pass
    while current_index < max_turn - 1:
        current_index += 1
        previous_index = number_map.get(next_number, False)
        if match_diff:
            next_value = match_diff
            match_diff = False
        else:
            next_value = 0
        if previous_index:
            match_diff = current_index - previous_index
            # If we find a duplicate store the difference of the previous value and the
            # most recent match
            next_number = match_diff
            number_map[next_value] = current_index
        else:
            # If we do not find a duplicate, store a zero
            next_number = 0
            number_map[next_value] = current_index
    return next_number


if __name__ == "__main__":
    INPUT = [0, 1, 4, 13, 15, 12, 16]
    # INPUT = TEST_INPUT
    print(both_parts(INPUT, 2020))
    print(both_parts(INPUT, 30000000))
