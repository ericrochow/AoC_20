#!/usr/bin/env python3

# TEST_INPUT = [0, 3, 6]
TEST_INPUT = [1, 3, 2]
# TEST_INPUT = [2, 1, 3]
# TEST_INPUT = [1, 2, 3]
# TEST_INPUT = [2, 3, 1]


# def part_one(number_list, max_turn):
def both_parts(number_list, max_turn):
    while len(number_list) < max_turn:
        last = number_list[-1]
        try:
            rev = number_list[::-1]
            last_index = rev[1:].index(last) + 1
            next_number = last_index
        except ValueError:
            next_number = 0
        number_list.append(next_number)
    return number_list[-1]


def part_two():
    pass


if __name__ == "__main__":
    INPUT = [0, 1, 4, 13, 15, 12, 16]
    INPUT = TEST_INPUT
    print(both_parts(INPUT, 2020))
    print(both_parts(INPUT, 30000000))
