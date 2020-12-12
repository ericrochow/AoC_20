#!/usr/bin/env python3


from utils import read_input


def part_one(cypher: list[int], preamble_len: int = 25) -> int:
    """
    Iterates over a list of integers to find the first value that cannot be created by
        adding 2 of the previous 25 unique numbers.

    First A slice is created containing the current number and the previous 25 numbers
        in the list. Next a list is created containing the absolute values of the
        differences between the current number and each of the previous 25 numbers in
        the list using a mapped lambda funciton. Finally, the unique difference values
        are compared against the unique values in the initial slice. If there is no
        overlap, this is the solution.

    Args:
      cypher: A list of integers containing the unique input for the user
      preamble_len: An integer specifying the preamble length (optional, defaults to
          25)
    Returns:
      An integer specifying the first value that cannot be created by the sum of 2
          unique numbers from the previous 25.
    """
    for index, entry in enumerate(cypher[preamble_len:], start=preamble_len):
        cypher_slice = cypher[index - preamble_len : index]
        differences = [x for x in map(lambda y: abs(entry - y), cypher_slice)]
        if set(differences).intersection(set(cypher_slice)) == set():
            return entry


def part_two(cypher: list[int], preamble_len: int = 25):
    """
    Iterates over a list of numbers to find contiguous entries that add up to the
        result of part_one() then sums the minimum and maxium values.

    List entries are continually added to a list until the sum of the list either
        matches or exceeds the output of part_one(). If the sum exceeds the output, the
        first entry is dropped.

    Args:
      cypher: A list of integers containing the unique input for the user
      preamble_len: An integer specifying the preamble length (optional, defaults to
          25)
    Returns:
      An integer specifying the sum of the minimum and maximum values in the list of
          contiguous values whose sum equals the output of part_one().
    """
    invalid_number = part_one(cypher, preamble_len=preamble_len)
    index = 0
    contiguous = []
    while index < len(cypher):
        contiguous_sum = sum(contiguous)
        if contiguous_sum < invalid_number:
            contiguous.append(cypher[index])
            index += 1
        elif contiguous_sum == invalid_number:
            return min(contiguous) + max(contiguous)
        elif contiguous_sum > 0:
            del contiguous[0]


if __name__ == "__main__":

    INPUT = [int(x) for x in read_input(9)]
    PREAMBLE_LEN = 25
    print(part_one(INPUT, PREAMBLE_LEN))
    print(part_two(INPUT, PREAMBLE_LEN))
