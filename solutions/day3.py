#!/usr/bin/env python

from utils import read_input


def plotter(plot, right, down):
    x_coord = 0
    y_coord = 0
    trees = 0

    while True:
        try:
            square = plot[y_coord][x_coord]
            if square == "#":
                trees += 1
            x_coord += right
            y_coord += down
        except IndexError:
            break
    return trees


def part_one(plot):
    return plotter(plot, 3, 1)


def part_two(plot):
    R1D1 = plotter(plot, 1, 1)
    R3D1 = plotter(plot, 3, 1)
    R5D1 = plotter(plot, 5, 1)
    R7D1 = plotter(plot, 7, 1)
    R1D2 = plotter(plot, 1, 2)
    return R1D1 * R3D1 * R5D1 * R7D1 * R1D2


if __name__ == "__main__":
    PLOT = [list(line * 1000) for line in read_input(3)]
    print(part_one(PLOT))
    print(part_two(PLOT))
