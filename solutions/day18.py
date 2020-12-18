#!/usr/bin/env python3


import ipdb  # noqa: F401
import re

from utils import read_input

TEST_INPUT = [
    "1 + 2 * 3 + 4 * 5 + 6",
    "1 + (2 * 3) + (4 * (5 + 6))",
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
    "5 + (8 * 3 + 9 + 3 * 4 * 3)",
]
# expect ["71", "51", "12240", "13632", "437"]


PAREN_RE = re.compile(r"\([^\(]+\)")
OPERATOR_RE = re.compile(r"[\+\*]")


def math_operation(expression: str) -> str:
    """
    Performs a match operation left to right regardless of normal mathmatical
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


def extract_parens(expression: str) -> str:
    """
    Extracts and evaluates mathematical operations within parenthesis.

    Args:
      expression: A string continaing a mathematic operation
    Returns:
      A string containing the original expression with the parenthesis broken down.
    """
    while "(" in expression:
        parens_deep = 0
        for index, value in enumerate(expression.split()):
            ipdb.set_trace()
            if value.startswith("("):
                expression_start = index
                parens_deep += value.count("(")
                ipdb.set_trace()
            elif value.endswith(")"):
                expression_end = index
                parens_deep -= value.count(")")
                ipdb.set_trace()
                if parens_deep == 0:
                    to_evaluate = (
                        " ".join(expression[expression_start : expression_end + 1])
                        .lstrip("(")
                        .rstrip(")")
                    )
                    ipdb.set_trace()
                    after = math_operation(to_evaluate)
                    expression = (
                        f"{' '.join(expression[0:expression_start])} {after}"
                        f"{' '.join(expression[expression_end + 1:])}"
                    )
                    continue
    ipdb.set_trace()
    return expression


def evaluate_expression(expression: str) -> str:
    """
    Addition and multiplication now have the same precedence so they are evaluated
        left-to-right.
    """
    pass


def part_one(ops: list):
    r = []
    for line in ops:
        line = extract_parens(line)
        r.append(math_operation(line))
    return r


def part_two():
    pass


if __name__ == "__main__":
    INPUT = read_input(18)
    INPUT = TEST_INPUT
    print(part_one(INPUT))
    print(part_two())
