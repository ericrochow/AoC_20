#!/usr/bin/env python3

from utils import read_input

TEST_INPUT = ["939", "7,13,x,x,59,x,31,19"]

TEST_INPUT_2 = ["100", "67,7,59,61"]

TEST_INPUT_3 = ["100", "67,x,7,59,61"]

TEST_INPUT_4 = ["100", "1789,37,47,1889"]


def enumerate_busses(bus_list: list) -> list:
    """"""
    en_list = list(enumerate(bus_list))
    while True:
        try:
            en_list.sort(key=lambda x: int(x[1]), reverse=True)
            print("Generated list")
            return en_list
        except ValueError:
            for idx, x in enumerate(en_list):
                if x[1] == "x":
                    del en_list[idx]


def part_one(earliest, bus_list):
    soonest_runs = {}
    busses = [int(bus) for bus in bus_list if bus != "x"]
    for bus in busses:
        bus_start = bus
        while bus_start < earliest:
            bus_start += bus
        soonest_runs[bus] = bus_start
    soonest_depart = min(soonest_runs.values())
    bus_id = [key for key in soonest_runs if soonest_runs[key] == soonest_depart][0]
    minutes_to_wait = soonest_depart - earliest
    return bus_id * minutes_to_wait


def part_two(bus_list):
    # TODO: Generate lists of departure times less than arbitrary max
    # Perform unions of bus`index` start times + index
    arbitrary_min = 100000000000000
    arbitrary_max = 1000000000000000
    # start_list = {x for x in range(arbitrary_min, arbitrary_max)}
    start_list = set()
    bus_list = enumerate_busses(bus_list)
    # for index, bus in enumerate(bus_list):
    for index, bus in bus_list:
        if bus != "x":
            if start_list:
                bus_starts = {x for x in start_list if (x + index) % int(bus) == 0}
                start_list.intersection_update(bus_starts)
            else:
                start_list = {
                    x
                    for x in range(arbitrary_min, arbitrary_max)
                    if (x + index) % int(bus) == 0
                }
    return start_list.pop()


if __name__ == "__main__":
    INPUT = read_input(13)
    # INPUT = TEST_INPUT_2
    EARLIEST = int(INPUT[0])
    BUS_LIST = [x for x in INPUT[1].split(",")]
    print(part_one(EARLIEST, BUS_LIST))
    print(part_two(BUS_LIST))
