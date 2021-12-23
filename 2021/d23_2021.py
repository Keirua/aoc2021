import aoc
import pprint
from collections import namedtuple, deque
from dataclasses import dataclass
from copy import deepcopy
pp = pprint.PrettyPrinter(indent=4)

# GameState = namedtuple("GameState", "map positions energy")
@dataclass
class GameState:
    map: list
    positions: list
    energy: int

    def __lt__(self, other):
        return self.energy.__lt__(other.energy)

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
    map = [list(l.rstrip()) for l in aoc.as_lines(input)]
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
    assert(amphipod in target_positions), amphipod
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

def target_room_is_walkable(gs, k):
    for t in target_positions[k]:
        if get_type(gs, t) not in [".", k]:
            return False
    return True


def walkable_neighbours(gs, p):
    """Return the neighbours, horizontal and vertical where one can move"""
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x, y = p
    return [(x + dx, y + dy) for (dx, dy) in offsets if get_type(gs, (x + dx, y + dy)) == "."]

forbidden_stops = [(3, 1), (5, 1), (7, 1), (9, 1)]
def find_possible_moves(gs: GameState, start):
    """Find the possible moves from a start position using floodfilling"""
    destinations = []
    visited = [start]
    queue = deque(walkable_neighbours(gs, start))
    amphipod = get_type(gs, start)
    if is_target_room(amphipod, start):
        # if all the amphipods of a given type have reached their room, they should not move anymore
        if all(get_type(gs, t) == amphipod for t in target_positions[amphipod]):
            return []
        # if an amphipod is in the bottom-most room, it should not move
        if start[1] == 3:
            return []

    while len(queue) > 0:
        t = queue.popleft()
        if t not in visited:
            visited.append(t)
            # From a room you can go to the hallway (if it’s an authorized spot)
            # or to your target room
            if is_room(start):
                if is_target_room(amphipod, t):
                    destinations.append(t)
                if is_hallway(t) and t not in forbidden_stops:
                    destinations.append(t)
            # an amphipod in the hallway can only move to a room,
            # but it has to be its target room, and there must only be amphipod of its kind or nothing
            if is_hallway(start) and is_target_room(amphipod, t) and target_room_is_walkable(gs, amphipod):
                destinations.append(t)

            # Generate other states
            for n in walkable_neighbours(gs, t):
                queue.append(n)

    return destinations



def move(gs, src, dst):
    gs.map[dst[1]][dst[0]] = gs.map[src[1]][src[0]]
    gs.map[src[1]][src[0]] = "."
    gs.positions.remove(src)
    gs.positions.append(dst)

def map_as_str(gs):
    s = ""
    for l in gs.map:
        s += "".join(l) + "\n"
    return s

def print_map(gs):
    print(map_as_str(gs))

def part1_bfs(gs):
    """attempt to solve part1 using BFS"""
    stk = [gs]
    visited = []
    wons = []
    best_won_score = None
    while len(stk) > 0:
        gs = stk.pop()
        if gs.map in visited:
            continue
        # print_map(gs)
        visited.append(gs.map)
        if is_won(gs):
            wons.append(gs)
            if best_won_score is None or gs.energy < best_won_score:
                best_won_score = gs.energy
                print(best_won_score)
            continue
        for p in gs.positions:
            new_positions = find_possible_moves(gs, p)
            for np in new_positions:
                gs2 = deepcopy(gs)
                gs2.energy += energy_cost(gs2, p, np)
                move(gs2, p, np)
                if gs2.map not in visited:
                    stk.append(gs2)
    print(best_won_score)
    pp.pprint(stk)

import heapq
def part1(gs):
    # def dijkstra_fast(grid, start=(0, 0), end=None):
    """faster dijkstra implementation using a priority queue"""
    # dist = {v: 1000000000000000 for v in grid.all_coords()}
    dist = {}
    prev = {}
    dist[map_as_str(gs)] = None
    Q = [(0, gs)]
    while len(Q) > 0:
        min_energy, min_gs = heapq.heappop(Q)
        # print(min_energy, min_gs)
        # we may provide an end node, if so we can break early
        if is_won(min_gs):
            print("minimum energy: ", min_energy)
            break
        # print_map(min_gs)
        # print(min_energy)
        curr_dist = None
        if map_as_str(min_gs) in dist:
            curr_dist = dist[map_as_str(min_gs)]
        if curr_dist is not None and min_energy > curr_dist:
            continue

        for p in min_gs.positions:
            new_positions = find_possible_moves(min_gs, p)
            # print("\t{!r}, {}".format(new_positions, curr_dist))
            for np in new_positions:
                gs2 = deepcopy(min_gs)
                energy2 = min_gs.energy + energy_cost(min_gs, p, np)
                move(gs2, p, np)
                gs2.energy = energy2
                if (curr_dist is not None and energy2 < curr_dist) or curr_dist is None:
                    dist[map_as_str(min_gs)] = energy2
                    prev[map_as_str(min_gs)] = gs2
                    heapq.heappush(Q, (energy2, gs2))
    return dist, prev


input = aoc.input_as_string(aoc.challenge_filename(23, 2021))
gs = parse(input)

assert (is_won(gs) == False)
assert (is_target_room("A", (1, 1)) == False)
assert (is_target_room("A", (2, 3)) == False)
assert (is_target_room("A", (3, 2)) == True)
print_map(gs)
# move(gs, (9, 2), (11, 1))
part1(gs) # 12769 is too low, 17357 too high, 24971 is too high, 15301 is not ok
# dijkstra says minimum energy:  10901 (in almost 10mn…)


# pp.pprint(gs.positions)
# move(gs, (3, 2), (1, 1))
# move(gs, (7, 2), (11, 1))
# move(gs, (7, 3), (10, 1))
# # print(find_possible_moves(gs, (3, 2)))
# print_map(gs)
# print(find_possible_moves(gs, (1, 1)))
# # print_map(gs)
# # pp.pprint(gs.positions)
# print(walkable_neighbours(gs, (1, 1)))