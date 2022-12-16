import re, pprint as pp, itertools as it
import typing
from functools import lru_cache

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


# @lru_cache(maxsize=None)
def part1(curr_valve: str, remaining_time: int = 30, pressure: int = 0, open_bitmask: int = 0) -> int:
    if remaining_time == 0:
        return pressure
    else:
        values = [pressure] # If we can open nothing new we may return the current pressure
        # if the current valve is not open, we can open it
        # We only do so if it adds some water
        if valves[curr_valve].flow_rate > 0 and not mapping[curr_valve] & open_bitmask:
            bitmask = mapping[curr_valve] | open_bitmask
            PRESSURE_AT[bitmask] = PRESSURE_AT[open_bitmask] + valves[curr_valve].flow_rate
            # the new pressure will take effect next time
            values.append(part1(curr_valve, remaining_time - 1, pressure + PRESSURE_AT[open_bitmask], bitmask))
        # We can take one step to reach another valve
        for v, d in valves[curr_valve].targets.items():
            values.append(part1(v, remaining_time - d, pressure + PRESSURE_AT[open_bitmask], open_bitmask))
        return max(values)

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


text = open(f"d16-sample.txt").read().strip()
# text = open(f"d16.txt").read().strip()
valves = parse(text)
# We need to simplify the graph so that we don’t move to useless locations
useful_valves = set([v.name for v in valves.values() if v.flow_rate > 0] + ["AA"])

new_graph = {}
for v in useful_valves:
    new_graph[v], _ = dijkstra(valves, v)
import pprint as pp
pp.pprint(new_graph)
# simplify(valves, useful_valves)
# valves = simplify(valves)
#
# curr_valve = "AA"
# print(valves)
# mapping = extract_name_mapping(valves)
# print(part1("AA", 30, 0, 0))
