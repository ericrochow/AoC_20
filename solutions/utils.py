#!/usr/bin/env python3

import os

import textfsm

HERE = os.path.abspath(os.path.dirname(__file__))


def read_input(day, output="list"):
    """"""
    input_file = os.path.join(HERE, "..", "inputs", f"day{day}.txt")
    with open(input_file, "r") as f:
        if output == "list":
            input_values = f.readlines()
            export = [x.strip("\n") for x in input_values]
        elif output == "blob":
            export = f.read()
    return export


def read_template(day):
    """"""
    template_file = os.path.join(HERE, "..", "templates", f"day{day}.textfsm")
    with open(template_file, "r") as f:
        template = textfsm.TextFSM(f)
    return template
