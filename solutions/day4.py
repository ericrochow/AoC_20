#!/usr/bin/env python3

import re

from utils import read_input

REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
OPTIONAL_KEYS = ["cid"]
VALID_EYES = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def create_kv_list(string_kv):
    data = {}
    for kv in string_kv.split():
        kvlist = kv.split(":")
        data[kvlist[0]] = kvlist[1]
    return data


def create_db(passport_list):
    passport_db = []
    for entry in passport_list:
        data = create_kv_list(entry)
        passport_db.append(data)
    return passport_db


def validate_keys(entry):
    return all(req in entry.keys() for req in REQUIRED_KEYS)


def validate_values(entry):
    if not validate_keys(entry):
        return False
    try:
        byr = int(entry["byr"])
        iyr = int(entry["iyr"])
        eyr = int(entry["eyr"])
        hgt = entry["hgt"]
        hcl = re.search(r"^#[0-9a-f]{6}$", entry["hcl"])
        ecl = re.search(r"^(amb|blu|brn|gry|grn|hzl|oth)$", entry["ecl"])
        pid = re.search(r"^\d{9}$", entry["pid"])
    except (KeyError, ValueError):
        print(entry)
        return False
    if byr < 1920 or byr > 2002:
        return False
    if iyr < 2010 or iyr > 2020:
        return False
    if eyr < 2020 or eyr > 2030:
        return False
    if hgt.endswith("cm"):
        try:
            hgt = int(re.search(r"\d{3}", hgt).group())
        except AttributeError:
            print(hgt)
            return False
        if hgt < 150 or hgt > 193:
            return False
    elif hgt.endswith("in"):
        try:
            hgt = int(re.search(r"\d{2}", hgt).group())
        except AttributeError:
            return False
        if hgt < 59 or hgt > 76:
            return False
    else:
        return False
    if not hcl:
        return False
    if not ecl:
        return False
    if not pid:
        return False
    return True


def part_one(passports):
    valid = 0
    invalid = 0
    passports = passports.replace("\n", " ")
    entries = passports.split("  ")
    passport_db = create_db(entries)
    for entry in passport_db:
        if validate_keys(entry):
            valid += 1
        else:
            invalid += 1
    print(f"Valid: {valid}\nInvalid: {invalid}")


def part_two(passports):
    valid = 0
    invalid = 0
    passports = passports.replace("\n", " ")
    entries = passports.split("  ")
    passport_db = create_db(entries)
    for entry in passport_db:
        if validate_values(entry):
            valid += 1
        else:
            invalid += 1
    print(f"Valid: {valid}\nInvalid: {invalid}")


if __name__ == "__main__":
    INPUT = read_input(4, output="blob")
    print(part_one(INPUT))
    print(part_two(INPUT))
