import aoc
import re, pprint, itertools as it
from collections import namedtuple

pp = pprint.PrettyPrinter(indent=4)

GameState = namedtuple("GameState", "map positions energy")
target_positions = {
    "A": [(3, 2), (3, 3)],
    "B": [(5, 2), (5, 3)],
    "C": [(7, 2), (7, 3)],
    "D": [(9, 2), (9, 3)],
}
energies = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}


def parse(input):
    map = aoc.as_lines(input)
    positions = {k: [] for k in "ABCD"}
    for j, line in enumerate(map):
        for i, cell in enumerate(line):
            if cell in "ABCD":
                positions[cell].append((i, j))
    return GameState(map, positions, 0)


def is_hallway(pos) -> bool:
    return pos[1] == 1


def is_target_room(amphipod, position) -> bool:
    """Returns True if *position* is the target room for amphipod A"""
    return position in target_positions[amphipod]


def is_won(positions) -> bool:
    """Check that the characters reached their correct positions"""
    for k in "ABCD":
        for p in positions[k]:
            if not is_target_room(k, p):
                return False
    return True


input = aoc.input_as_string(aoc.challenge_filename(23, 2021))
gs = parse(input)

assert (is_won(gs.positions) == False)
assert (is_target_room("A", (1, 1)) == False)
assert (is_target_room("A", (2, 3)) == False)
assert (is_target_room("A", (3, 2)) == True)
pp.pprint(gs.map)
pp.pprint(gs.positions)
# map, positions = parse(input)
# pp.pprint(positions)
# pp.pprint(map)
