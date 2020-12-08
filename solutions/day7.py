#!/usr/bin/env python3

from collections import deque

from utils import read_input


def build_db(rules):
    simple_db = {}
    for rule in rules:
        color = rule.split(" bag")[0]
        contents = rule.split("contain")[1:][0].split(",")
        simple_db[color] = {}
        for i in contents:
            sliced_iter = i.strip().split(" ")
            qty = sliced_iter[0]
            content_color = " ".join(sliced_iter[1:-1])
            try:
                simple_db[color][content_color] = int(qty)
            except ValueError:
                pass
    return simple_db


def find_color(rules, color):
    options = [x for x in rules if color in x]
    colors = {color.split(" bag")[0] for color in options}
    return colors


def part_one(rules):
    initial_options = find_color(rules, "shiny gold")
    pre, post = set(), set()
    pre.update(initial_options)
    while pre != post:
        pre.update(post)
        for color in pre:
            colors = find_color(rules, color)
            post.update(pre)
            post.update(colors)
    post.remove("shiny gold")
    return len(set(post))


def part_two_bak(rules):
    bags = 1
    simple_db = build_db(rules)
    to_look_up = deque()
    for bag_inv in simple_db.get("shiny gold"):
        bags += bag_inv["qty"]
        to_look_up.appendleft(bag_inv["name"])
    while True:
        if to_look_up:
            color = to_look_up.pop()
            # pp(simple_db.get("shiny gold"))
            for color in to_look_up:
                more_to_look_up = deque()
                for bag_inv in simple_db.get(color):
                    bags += bag_inv["qty"]
                    more_to_look_up.appendleft(bag_inv["name"])
            to_look_up = more_to_look_up
        else:
            break
    return bags


def part_two(rules):
    simple_db = build_db(rules)

    total_bags_count = {}

    def count_bags_inside(bag_to_count):
        current_bag = simple_db.get(bag_to_count)
        bags_inside = []
        for bag in current_bag:
            bags_inside.append(current_bag[bag])
            if total_bags_count.get(bag):
                bags_inside.append(total_bags_count[bag] * current_bag[bag])
            else:
                bags_inside.append(count_bags_inside(bag) * current_bag[bag])
        total_bags = sum(bags_inside)
        total_bags_count[bag_to_count] = total_bags
        return total_bags

    return count_bags_inside("shiny gold")


if __name__ == "__main__":
    INPUT = read_input(7)
    print(part_one(INPUT))
    print(part_two(INPUT))
