import aoc
import re, pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(21, 2021))
test_input = """Player 1 starting position: 4
Player 2 starting position: 8
"""


def parse(input):
    starts = re.findall(r"Player (\d+) starting position: (\d+)", input)
    players = {}
    for s in starts:
        nb, pos = int(s[0]) - 1, int(s[1])
        players[nb] = pos
    return players


dice_value = 0


def roll_dice():
    global dice_value
    dice_value += 1
    if dice_value > 100:
        dice_value = 1
    return dice_value


def play(players):
    # player 1 goes first
    current = 0
    # Players' scores start at 0
    scores = { 0: 0, 1: 0}
    done = False
    nb_rolls = 0
    while not done:
        # On each player's turn, the player rolls the die three times and adds up the results.
        three_dices = [roll_dice(), roll_dice(), roll_dice()]
        sum3 = sum(three_dices)
        nb_rolls += 3

        #  Then, the player moves their pawn that many times forward around the track
        # that is, moving clockwise on spaces in order of increasing value, wrapping back around to 1 after 10
        players[current] = players[current] + sum3
        while players[current] > 10:
            players[current] -= 10
        # After each player moves, they increase their score by the value of the space their pawn stopped on
        scores[current] += players[current]
        print("player {} rolls {!r} and moves to space {} for a total score of {}".format(1+current, three_dices, players[current], scores[current]))

        if scores[current] >= 1000:
            print("positions:")
            pp.pprint(players)
            print("scores:")
            pp.pprint(scores)
            print("nb roll:")
            pp.pprint(nb_rolls)
            return scores[(1 + current) % 2] * nb_rolls
            done = True
        current = (1 + current) % 2


pp.pprint(input)
players = (parse(input))
test_players = (parse(test_input))
# assert (play(test_players) == 739785)
print(play(players))  # 702723 is too low
