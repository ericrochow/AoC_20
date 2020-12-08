#!/usr/bin/env python3

from utils import read_input

ACCUMULATOR = 0
CURRENT_POS = 0

# TEST_INSTRUCTIONS = (
# "nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6"
# )


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
        # stop_sign = parse_line(temp_instructions[-1])
        instruction = parse_line(temp_instructions[CURRENT_POS])
        while operations < 500:
            # print(ACCUMULATOR)
            # print(CURRENT_POS)
            operations += 1
            process_instruction(instruction)
            try:
                instruction = parse_line(temp_instructions[CURRENT_POS])
                # print(instruction)
            # if instruction == stop_sign:
            except IndexError:
                # print("MATCH")
                # process_instruction(instruction)
                return ACCUMULATOR
        # print(f"Line {line} wasn't it.")


if __name__ == "__main__":
    INPUT = read_input(8)
    # INPUT = TEST_INSTRUCTIONS.split("\n")
    print(part_one(INPUT))
    print(part_two(INPUT))
