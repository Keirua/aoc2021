import aoc
import pprint
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
    positions = []
    for j, line in enumerate(map):
        for i, cell in enumerate(line):
            if cell in "ABCD":
                positions.append((i, j))
    return GameState(map, positions, 0)


def is_hallway(pos) -> bool: return pos[1] == 1
def is_room(pos) -> bool: return not is_hallway(pos)
def is_empty(gs, pos) -> bool: return get_type(gs, pos) == "."


def is_target_room(amphipod, position) -> bool:
    """Returns True if *position* is the target room for amphipod A"""
    return position in target_positions[amphipod]


def is_won(gs: GameState) -> bool:
    """Check that all the characters reached their correct positions"""
    for p in gs.positions:
        if not is_target_room(get_type(gs, p), p):
            return False
    return True


def manhattan_distance(p1, p2) -> int:
    """manhattan distance between p1 and p2"""
    return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])

def get_type(gs, p):
    """return the amphipod type in a given cell"""
    return gs.map[p[1]][p[0]]


def energy_cost(gs, p1, p2) -> int:
    """compute the total energy cost to move from p1 to p2, using the appropriate energy type"""
    return energies[get_type(gs, p1)] * manhattan_distance(p1, p2)

from copy import deepcopy
def generate_states(s: GameState):

    for p in s.positions:
        type = s.map[p[1]][p[0]]
        # an amphipod in the hallway can only move to a room, and to its target room
        if is_hallway(p):
            pass
        # if it is in its target room it can move once cell down
        if is_target_room(type, p):
            pass
        # if it is in a regular room, it can move in the valid cell of the hallway
        if is_room(p) and not is_target_room(type, p):
            valid_hallway_x_stop_positions = [1, 2, 4, 6, 8, 10, 11]
            y_hallway = 1
            for x in valid_hallway_x_stop_positions:
                if is_empty(gs, p):
                    gs2 = deepcopy(gs)






input = aoc.input_as_string(aoc.challenge_filename(23, 2021))
gs = parse(input)

assert (is_won(gs) == False)
assert (is_target_room("A", (1, 1)) == False)
assert (is_target_room("A", (2, 3)) == False)
assert (is_target_room("A", (3, 2)) == True)
pp.pprint(gs.map)
pp.pprint(gs.positions)
