#!/usr/bin/env python3

from copy import deepcopy
import ipdb
from itertools import product

from utils import read_input

TEST_INPUT = [".#.", "..#", "###"]


def define_neighbors(x: int, y: int, z: int) -> list:
    """
    Defines a list of coordinates to consider neighbors.

    Args:
      x: An integer specifying the starting x coordinate
      y: An integer specifying the starting y coordinate
      z: An integer specifying the starting z coordinate
    Returns:
      A list of coordinates
    """
    diffs = range(-1, 2)
    coords = []
    # might need to add some if guards (if x > 0) (if x < len(blah) etc)
    xdiffs = (x + diff for diff in diffs)
    ydiffs = (y + diff for diff in diffs)
    zdiffs = (z + diff for diff in diffs)
    neighbors = product(xdiffs, ydiffs, zdiffs)
    for index, neighbor in enumerate(neighbors):
        if neighbor != (x, y, z) and all(c >= 0 for c in neighbor):
            coords.append(neighbor)
    return coords


def define_cube_slice(grid_input: list) -> dict:
    """
    Defines a 2-dimensional slice of the cube.

    Args:
      grid_input: A list of strings with the text representation of active or inactive
          cubes
    Returns:
      A dict specifying the z-axis as the key and a list (y-axis) of lists (x-axis) as
          the value.
    """
    pad = (20 - len(grid_input[0])) // 2
    blank_grid = [["."] * 20] * 20
    grid_output = [["."] * 20] * 6
    for line in grid_input:
        line = ["."] * pad + line + ["."] * pad
        if len(line) % 2 == 1:
            line.append(".")
        grid_output.append(line)
    grid_output += [["."] * 20] * 6
    big_cube = {}
    for i in range(0, 21):
        big_cube[i] = blank_grid
    big_cube[10] = grid_output
    return big_cube


def simulate_change(pocket: dict) -> dict:
    """
    Simulates a round of cube status changes in the pocket dimension.

    If a cube is active (#) and exactly 2 or 3 of its neighbors are also active (#), the
        cube remains active (#). Otherwise it becomes inactive (.).

    If a cube is inactive (.) but exactly 3 of its neighbors are active (#), the cube
        becomes active (#). Otherwise, the cube remains inactive (.).

    A neighbor is defined as any of the other cubes where any of their coordinates
        differ by at most 1. e.g. x=1,y=2,z=3 would be neighbors with x=2,y=2,z=2

    Args:
      pocket:
    """
    new_pocket = deepcopy(pocket)
    for zindex, zval in pocket.items():
        for yindex, yval in enumerate(zval):
            for xindex, xval in enumerate(yval):
                active_neighbors = 0
                neighbor_coords = define_neighbors(xindex, yindex, zindex)
                for x, y, z in neighbor_coords:
                    try:
                        if pocket[z][y][x] == "#":
                            print("Coord: ", zindex, yindex, xindex)
                            print("Neighbor: ", z, y, x)
                            active_neighbors += 1
                            ipdb.set_trace()
                    except (IndexError, KeyError):
                        pass
                if xval == "." and active_neighbors == 3:
                    print(pocket[zindex][yindex][xindex])
                    print(new_pocket[zindex][yindex][xindex])
                    print("Activating", zindex, yindex, xindex)
                    new_pocket[zindex][yindex][xindex] = "#"
                    print(pocket[zindex][yindex][xindex])
                    print(new_pocket[zindex][yindex][xindex])
                elif xval == "#" and active_neighbors not in [2, 3]:
                    print("Deactivating", z, y, x)
                    new_pocket[zindex][yindex][xindex] = "."
    return new_pocket


def part_one(grid_input: list):
    pocket = define_cube_slice(grid_input)
    for _ in range(0, 6):
        pocket = simulate_change(pocket)
        ipdb.set_trace()
    return pocket


def part_two(grid_input: list):
    # pocket = define_cube_slice(grid_input)
    pass


if __name__ == "__main__":
    INPUT = read_input(17)
    INPUT = TEST_INPUT
    print(part_one(INPUT))
    print(part_two(INPUT))
