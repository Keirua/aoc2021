import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(21, 2021))
test_input = """Player 1 starting position: 4
Player 2 starting position: 8
"""

def parse(input):
    starts = re.findall(r"Player (\d+) starting position: (\d+)", input)
    players = {}
    for s in starts:
        nb, pos = int(s[0])-1, int(s[1])
        players[nb] = pos
    return players

pp.pprint(input)
pp.pprint(parse(input))
pp.pprint(parse(test_input))
