#!/usr/bin/env python3

import re

from utils import read_input


def math_operation_no_precedence(expression: str) -> str:
    """
    Performs a math operation left to right regardless of normal mathmatical
        precendence of multiplication over addition. It is expected that the expression
        does not have parenthesis.

    Args:
      expression: A string containing a mathmatical expression.
    Returns:
      A string containing the final value of the expression.
    """
    elements = expression.split()
    final = 0
    for index, value in enumerate(elements):
        if index == 0:
            final = int(value)
        elif index % 2 == 0:
            if elements[index - 1] == "+":
                final += int(value)
            elif elements[index - 1] == "*":
                final *= int(value)
    return str(final)


def math_operation_reverse_precedence(expression: str) -> str:
    """
    Performs a math operation reversing the precendence of multiplication over
    addition by prioritising addition over multiplication. It is expected that the
    expression does not have parenthesis.

    Args:
      expression: A string containing a mathmatical expression.
    Returns:
      A string containing the final value of the expression.
    """
    elements = expression.split()
    addition_evaluated = []
    final = 1
    for index, value in enumerate(elements):
        if value == "*":
            addition_evaluated.append(value)
        elif index == 0:
            addition_evaluated.append(int(value))
        elif index % 2 == 0 and index >= 2 and elements[index - 1] == "+":
            if addition_evaluated[-1] in ["+", "*"]:
                addition_evaluated.append(int(value))
            else:
                addition_evaluated[-1] += int(value)
        elif addition_evaluated[-1] == "*":
            addition_evaluated.append(int(value))
    for index, value in enumerate(addition_evaluated):
        if index == 0:
            final *= int(value)
        if index % 2 == 0 and index >= 2 and addition_evaluated[index - 1] == "*":
            final *= int(value)
    return str(final)


def extract_parens(expression: str, part: int) -> str:
    """
    Recursively resolve math operations within parenthesis until there are no more
        parenthesis.

    Args:
      expression: The original mathematical operation to evaluate
      part: An integer specifying the part whose instructions to follow
    Returns:
      A string with the simplified expression.
    """
    paren_re = re.compile(r"\([^\(]+?\)")
    simplified = expression
    while "(" in simplified:
        parens = paren_re.findall(simplified)
        for paren in parens:
            expr = paren.lstrip("(").rstrip(")")
            if part == 1:
                solved = math_operation_no_precedence(expr)
            elif part == 2:
                solved = math_operation_reverse_precedence(expr)
            simplified = simplified.replace(paren, solved)
    return simplified


def part_one(ops: list) -> int:
    results = []
    for line in ops:
        line = extract_parens(line, 1)
        solved = math_operation_no_precedence(line)
        results.append(math_operation_no_precedence(solved))
    return sum(int(r) for r in results)


def part_two(ops: list) -> int:
    results = []
    for line in ops:
        line = extract_parens(line, 2)
        solved = math_operation_reverse_precedence(line)
        results.append(math_operation_reverse_precedence(solved))
    return sum(int(r) for r in results)


if __name__ == "__main__":
    INPUT = read_input(18)
    print(part_one(INPUT))
    print(part_two(INPUT))
