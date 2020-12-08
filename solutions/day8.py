#!/usr/bin/env python3

from utils import read_input

ACCUMULATOR = 0
CURRENT_POS = 0


def parse_line(line):
    line = line.split(" ")
    operation = line[0]
    action = int(line[1])
    return operation, action


def update_accumulator(value):
    global ACCUMULATOR
    ACCUMULATOR += value


def process_instruction(instruction):
    global CURRENT_POS
    if instruction[0] == "acc":
        CURRENT_POS += 1
        update_accumulator(instruction[1])
    elif instruction[0] == "jmp":
        CURRENT_POS += instruction[1]
    elif instruction[0] == "nop":
        CURRENT_POS += 1


def toggle_operation(instruction):
    split_instruction = instruction.split(" ")
    if split_instruction[0] == "nop":
        split_instruction[0] = "jmp"
    elif split_instruction[0] == "jmp":
        split_instruction[0] = "nop"
    return " ".join(split_instruction)


def part_one(instructions):
    global CURRENT_POS
    history = []
    instruction = parse_line(instructions[CURRENT_POS])
    while CURRENT_POS not in history:
        history.append(CURRENT_POS)
        process_instruction(instruction)
        instruction = parse_line(instructions[CURRENT_POS])
    return ACCUMULATOR


def part_two(instructions):
    global CURRENT_POS
    global ACCUMULATOR
    for line in range(0, len(instructions)):
        ACCUMULATOR = 0
        CURRENT_POS = 0
        operations = 0
        temp_instructions = instructions.copy()
        temp_instructions[line] = toggle_operation(temp_instructions[line])
        instruction = parse_line(temp_instructions[CURRENT_POS])
        while operations < 500:
            operations += 1
            process_instruction(instruction)
            try:
                instruction = parse_line(temp_instructions[CURRENT_POS])
            except IndexError:
                return ACCUMULATOR


if __name__ == "__main__":
    INPUT = read_input(8)
    print(part_one(INPUT))
    print(part_two(INPUT))
