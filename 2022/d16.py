import re, pprint as pp, itertools as it
import typing
from functools import lru_cache
from collections import deque

class Valve:
    def __init__(self, name: str, flow_rate: int, targets: typing.List[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.targets = {t: 1 for t in targets}

    def __repr__(self):
        return f"<Valve name={self.name} flow={self.flow_rate} targets={','.join(self.targets.keys())}>"


def parse(text: str) -> typing.Dict[str, Valve]:
    lines = text.split("\n")
    valves = {}

    for line in lines:
        # Valve JT has flow rate=21; tunnels lead to valves ZG, FA
        item = re.findall(r"([A-Z]{2}|\d+)", line)
        valves[item[0]] = Valve(item[0], int(item[1]), item[2:])
    return valves


def extract_name_mapping(valves: typing.Dict[str, Valve]) -> typing.Dict[str, int]:
    """Turn all the valve names into a bitmask. Since there are 58 values, it fits in 64 bits"""
    mapping = {}
    names = set()
    for k, v in valves.items():
        names |= set([k]) | set(v.targets)
    names = sorted(names)
    for i, n in enumerate(names):
        mapping[n] = 1 << i
    return mapping

def simplify(valves):
    """
    remove nodes that have a flow of 0 (we dont want to turn them on) and
    increase the distances from those nodes to others ?
    """
    return valves


PRESSURE_AT = {0: 0}

import heapq
def dijkstra(valves, start=(0, 0)):
    """Dijkstra's algorithm implementation using a priority queue"""
    dist = { v: 1000000000000000 for v in valves.keys()}
    dist[start] = 0
    prev = {v: None for v in valves.keys()}

    # The queue of nodes we will consider, with one starting point:
    Q = [(0, start)]
    while len(Q) > 0:
        min_dist, min_coord = heapq.heappop(Q)
        if min_dist > dist[min_coord]:
            continue
        for neighbour in valves[min_coord].targets:
            new_distance = min_dist + 1
            if new_distance < dist[neighbour]:
                dist[neighbour] = new_distance
                prev[neighbour] = min_coord
                heapq.heappush(Q, (new_distance, neighbour))
    return dist, prev

@lru_cache(maxsize=None)
def part1_dp(curr_valve: str, remaining_time: int = 30, pressure: int = 0, open_bitmask: int = 0) -> int:
    global useful_valves, mapping, distances
    if remaining_time == 0:
        return pressure
    else:
        # If we can open nothing new we may return the current pressure
        values = [pressure]
        # if the current valve is not open, we can open it
        # We only do so if it adds some water
        if valves[curr_valve].flow_rate > 0:
            if not mapping[curr_valve] & open_bitmask:
                bitmask = mapping[curr_valve] | open_bitmask
                PRESSURE_AT[bitmask] = PRESSURE_AT[open_bitmask] + valves[curr_valve].flow_rate
                # the new pressure will take effect next time
                values.append(part1_dp(curr_valve, remaining_time - 1, pressure + PRESSURE_AT[open_bitmask], bitmask))

        # We can take one step to reach another valve
        for v in useful_valves - {curr_valve}:
            dist = distances[curr_valve][v]
            if remaining_time - dist >= 0:
                values.append(part1_dp(v, remaining_time - dist, pressure + dist * PRESSURE_AT[open_bitmask], open_bitmask))
        return max(values)

@lru_cache(maxsize=None)
def pressure_at(open_valves):
    global valves
    return sum([valves[v].flow_rate for v in open_valves])

# def part1_dfs(curr_valve: str, remaining_time: int = 30, pressure: int = 0) -> int:
#     Q = deque([(pressure, remaining_time, frozenset(), curr_valve)])
#     global useful_valves, mapping, distances, valves
#     SEEN = []
#     best = 0
#     while len(Q) > 0:
#         pressure, remaining_time, open_valves, curr_valve = Q.popleft()
#         if remaining_time == 0:
#             best = max(best, pressure)
#         state = (pressure, remaining_time, open_valves, curr_valve)
#         # print(state)
#         if len(SEEN) % 10_000 == 0:
#             # print(SEEN)
#             print(len(SEEN))
#         if state in SEEN:
#             continue
#
#         SEEN.append(state)
#
#         # if the current valve is not open, we can open it
#         # We only do so if it adds some water
#         if valves[curr_valve].flow_rate > 0:
#             if not curr_valve in open_valves:
#                 new_open_valves = frozenset(open_valves | set([curr_valve]))
#                 # the new pressure will take effect next time
#                 # values.append(part1_dp(curr_valve, remaining_time - 1, pressure + PRESSURE_AT[open_bitmask], bitmask))
#                 Q.append((pressure + pressure_at(open_valves), remaining_time - 1, new_open_valves, curr_valve))
#
#         # If all the valves are open, no need to move anymore, we can compute the max pressure from here
#         if len(useful_valves - open_valves) == 0:
#             # print("everything is open", len(useful_valves - open_valves))
#             max_pressure = pressure + pressure_at(open_valves)*remaining_time
#             best = max(best, max_pressure)
#             continue
#         else:
#
#             # Otherwise we can take one step to reach another useful but not-yet-open valve
#             for v in useful_valves - {curr_valve} - open_valves:
#                 dist = distances[curr_valve][v]
#                 if remaining_time - dist >= 0:
#                     Q.append((pressure + dist * pressure_at(open_valves), remaining_time - dist, open_valves, v))
#             # If we can open nothing new we can update the pressures the current pressure
#             Q.append((pressure + pressure_at(open_valves), remaining_time - 1, open_valves, curr_valve))
#     return best


text = open(f"d16-sample.txt").read().strip()
text = open(f"d16.txt").read().strip()
valves = parse(text)
# pp.pprint(valves)
# We need to simplify the graph so that we don’t move to useless locations,
# so we’ll only take care of the valves with a flow_rate > 0
useful_valves = {k for k, v in valves.items() if v.flow_rate > 0}
# print(useful_valves)
# Now we can compute the distances between the interesting nodes (those that we can open)
# We include the starting node
distances = {}
for v in useful_valves | {"AA"}:
    dist, _ = dijkstra(valves, v)
    distances[v] = {name: length for name, length in dist.items() if name in useful_valves and name != v}
# pp.pprint(distances)
def dump(valves):
    print("digraph some_graph {\n node [shape=box];\n")
    for v in valves.keys():
        valve = valves[v]
        for t in valves[v].targets:
            print(f"\t\"{valve.name} - {valve.flow_rate}\" -> \"{t} - {valves[t].flow_rate}\"")
    print("}")

def dump_simplified(valves, useful_valves):
    print("digraph some_graph {\n node [shape=box];\n")
    for v in useful_valves | {"AA"}:
        valve = valves[v]
        for t in useful_valves - {v}:
            print(f'\t"{v} - {valve.flow_rate}" -> "{t} - {valves[t].flow_rate}" [label="{distances[v][t]}"]')
    print("}")
# dump_simplified(valves, useful_valves)
# dump(valves)
mapping = extract_name_mapping(valves)
print(part1_dfs("AA", 30, 0))
# print(part1_dp("AA", 30, 0, 0))
