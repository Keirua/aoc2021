import aoc
import re, pprint
from functools import lru_cache
import itertools as it

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
    dice_value = (dice_value % 100) + 1
    return dice_value


def play(players, debug=False):
    # player 1 goes first
    current = 0
    # Players' scores start at 0
    scores = {0: 0, 1: 0}
    done = False
    nb_rolls = 0
    while not done:
        # On each player's turn, the player rolls the die three times and adds up the results.
        three_dices = [roll_dice(), roll_dice(), roll_dice()]
        sum3 = sum(three_dices)
        nb_rolls += 3
        #  Then, the player moves their pawn that many times forward around the track
        # that is, moving clockwise on spaces in order of increasing value, wrapping back around to 1 after 10
        players[current] = next_position(players[current], sum3)
        # After each player moves, they increase their score by the value of the space their pawn stopped on
        scores[current] += players[current]
        if debug:
            print("player {} rolls {!r} and moves to space {} for a total score of {}".format(1 + current, three_dices,
                                                                                              players[current],
                                                                                              scores[current]))

        if scores[current] >= 1000:
            if debug:
                print("positions:")
                pp.pprint(players)
                print("scores:")
                pp.pprint(scores)
                print("nb roll:")
                pp.pprint(nb_rolls)
            return scores[1 - current] * nb_rolls
            done = True
        current = (1 - current)


@lru_cache(maxsize=None)
def next_position(current_position: int, three_dices: int) -> int:
    """The new position on the board, once you move"""
    return (current_position + three_dices - 1) % 10 + 1


@lru_cache(maxsize=None)
def part2(p0, p1, s0, s1, current=0):
    """
    p0, p1 are the positions of the players 0 and 1
    s0, s1 are the scores of the players 0 and 1
    current is the index of the current player
    """
    if s0 >= 21:
        return [1, 0]  # 1 more win for player 0
    if s1 >= 21:
        return [0, 1]
    ans = [0, 0]

    # Generate all the new dices
    for a, b, c in it.product(range(1, 4), range(1, 4), range(1, 4)):
        # then we update the positions and scores depending on who’s turn it is to play
        if current == 0:
            new_p0 = next_position(p0, a + b + c)
            new_s0 = s0 + new_p0
            # we search for the winner in this sub-universe
            # (thanks lru_cache: there are not that many possibilities, so a lot of duplicates)
            partial = part2(new_p0, p1, new_s0, s1, 1)
        else:
            new_p1 = next_position(p1, a + b + c)
            new_s1 = s1 + new_p1
            partial = part2(p0, new_p1, s0, new_s1, 0)
        # and we update the global winner scoreboard
        ans = [ans[0] + partial[0], ans[1] + partial[1]]
    return ans


players = (parse(input))
test_players = (parse(test_input))
assert (play(test_players) == 739785)
print(play(players))  # 702723 is too low
assert (max(part2(4, 8, 0, 0)) == 444356092776315), part2(4, 8, 0, 0)
print(max(part2(10, 9, 0, 0)))
