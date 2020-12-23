#!/usr/bin/env python3

from collections import deque
from copy import deepcopy

from utils import read_input

TEST_INPUT = [
    "Player 1:",
    "9",
    "2",
    "6",
    "3",
    "1",
    "",
    "Player 2:",
    "5",
    "8",
    "4",
    "7",
    "10",
]

TEST_INPUT_2 = [
    "Player 1:",
    "43",
    "19",
    "",
    "Player 2:",
    "2",
    "29",
    "14",
]


def create_decks(file_input: list) -> dict:
    """
    Reads the file input and sorts the cards into the appropriate decks.

    Args:
        file_input: A list of lines from the input file
    Returns:
        A dict containing each player's deck.
    """
    decks = {}
    for line in file_input:
        if line.startswith("Player"):
            key = line.strip(":")
            decks[key] = deque()
        elif line:
            decks[key].append(int(line))
    return decks


def simulate_round(decks: dict) -> dict:
    """
    Simulates a round of 'Combat' by comparing the top card of each deck. The deck with
        the higher card places that card under its' deck followed by the other deck's
        card.
    Args:
        decks: A dict containing the deck of each player
    Returns:
        A dict containing the updated decks.
    """
    p1_card = decks["Player 1"].popleft()
    p2_card = decks["Player 2"].popleft()
    if p1_card > p2_card:
        decks["Player 1"].append(p1_card)
        decks["Player 1"].append(p2_card)
    elif p2_card > p1_card:
        decks["Player 2"].append(p2_card)
        decks["Player 2"].append(p1_card)
    return decks


def simulate_recursive_round(decks: dict, history: list) -> tuple:
    if decks in history:
        decks["Player 2"] = deque()
        return decks, history
    history.append(deepcopy(decks))
    p1_card = decks["Player 1"].popleft()
    p2_card = decks["Player 2"].popleft()
    if p1_card <= len(decks["Player 1"]) and p2_card <= len(decks["Player 2"]):
        p1_subdeck = list(decks["Player 1"])[0:p1_card]
        p2_subdeck = list(decks["Player 2"])[0:p2_card]
        if max(p1_subdeck) > max(p2_subdeck):
            decks["Player 1"].append(p1_card)
            decks["Player 1"].append(p2_card)
        else:
            subdecks = {"Player 1": deque(p1_subdeck), "Player 2": deque(p2_subdeck)}
            subgame_winner = simulate_recursive_game(subdecks)["player"]
            if subgame_winner == "Player 1":
                decks["Player 1"].append(p1_card)
                decks["Player 1"].append(p2_card)
            elif subgame_winner == "Player 2":
                decks["Player 2"].append(p2_card)
                decks["Player 2"].append(p1_card)
        return decks, history
    elif p1_card > p2_card:
        decks["Player 1"].append(p1_card)
        decks["Player 1"].append(p2_card)
    elif p2_card > p1_card:
        decks["Player 2"].append(p2_card)
        decks["Player 2"].append(p1_card)
    return decks, history


def simulate_standard_game(decks: dict) -> deque:
    """
    Simulates a standard game of 'Combat' by running rounds until one of the players
        holds all of the cards.

    Args:
        decks: A dict containing each player's starting deck
    Returns:
        A deque containing the winner's deck.
    """
    while len(decks["Player 1"]) > 0 and len(decks["Player 2"]) > 0:
        decks = simulate_round(decks)
    for player, deck in decks.items():
        if deck:
            return {"player": player, "deck": deck}


def simulate_recursive_game(decks: dict) -> deque:
    """
    Simulates a game of 'Recursive Combat'.

    Args:
        decks: A dict containing each player's starting deck
    Returns:
        A deque containing the winner's deque.
    """
    history = []
    while len(decks["Player 1"]) > 0 and len(decks["Player 2"]) > 0:
        decks, history = simulate_recursive_round(decks, history)
    for player, deck in decks.items():
        if deck:
            return {"player": player, "deck": deck}


def calculate_score(winner_deck: deque) -> int:
    """
    Calculates the score by multiplying each card in the deck by its position starting
        at the bottom.

    Args:
        winner_deck: A deque contining the contents of the winner's deck
    Returns:
        An integer specifying the winner's score.
    """
    multiplier, score = 0, 0
    while len(winner_deck) > 0:
        multiplier += 1
        score += winner_deck.pop() * multiplier
    return score


def part_one(file_input: list) -> int:
    decks = create_decks(file_input)
    winner = simulate_standard_game(decks)
    winner_deck = winner["deck"]
    return calculate_score(winner_deck)


def part_two(file_input: list) -> int:
    decks = create_decks(file_input)
    winner_deck = simulate_recursive_game(decks)["deck"]
    return calculate_score(winner_deck)


if __name__ == "__main__":
    INPUT = read_input(22)
    # INPUT = TEST_INPUT
    print(part_one(INPUT))
    print(part_two(INPUT))
