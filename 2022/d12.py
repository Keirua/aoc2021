import pprint
from collections import deque
from grid import *
pp = pprint.PrettyPrinter(indent=4)

class CustomGrid(Grid):
    def __init__(self, w=0, h=0, lines=[]):
        super().__init__(w, h, lines)
        self.s = None
        self.e = None
        self.all_As = []

    def search_start_end(self, inp):
        for y, line in enumerate(inp.split("\n")):
            for x, c in enumerate(line):
                if c == 'a':
                    self.all_As.append((x, y))
                if c == 'S':
                    self.s = (x, y)
                if c == 'E':
                    self.e = (x, y)

    def valid_neighbours(self, p):
        return [k for k in self.neighbours4(p) if self[k] <= self[p]+1]

    @classmethod
    def from_input(cls, inp):
        g = cls.from_lines([[ord(c.lower())-ord('a') for c in line] for line in inp.split("\n")])
        g.search_start_end(inp)
        g[g.e] = ord('z') - ord('a') # Target node has elevation Z
        return g

    def __str__(self):
        return f"{super().__str__()}\n{self.s} -> {self.e}"

import heapq
def dijkstra(grid, start=(0, 0), end=None):
    """Dijkstra's algorithm implementation using a priority queue"""
    # Initial state:
    #  - all the distances to the starting node are maximal
    #    (except the starting node: it has a distance of 0 to itself).
    #  - all the ancestors are non-existing
    dist = { v: 1000000000000000 for v in grid.all_coords()}
    dist[start] = 0
    prev = {v: None for v in grid.all_coords()}

    # The queue of nodes we will consider, with
    Q = [(0, start)]
    while len(Q) > 0:
        # We consider the "cheapest" node, that is the node with the lowest cost.
        # We store the tuples (cost, position). In this context, heapq.heappop compares on the cost
        # https://docs.python.org/3.11/library/heapq.html#basic-examples
        min_dist, min_coord = heapq.heappop(Q)

        # we may provide an end node, if so we can break early
        if end is not None and min_coord == end:
            break

        if min_dist > dist[min_coord]:
            continue

        for neighbour in grid.valid_neighbours(min_coord):
            new_distance = min_dist + 1
            # If we found a better path, we update both the cost and the predecessor
            # and add this node to the queue
            if new_distance < dist[neighbour]:
                dist[neighbour] = new_distance
                prev[neighbour] = min_coord
                heapq.heappush(Q, (new_distance, neighbour))

    return dist, prev

def build_itinerary(prev, start, end):
    # build the itinerary backwards, by taking the parents until we reach the start
    history = [end]
    while history[-1] != start:
        if history[-1] in prev.keys():
            history.append(prev[history[-1]])
        else:
            raise ValueError("impossible move!")
    # reverse the history
    return history[::-1]

# Debug itinerary
def build_debug_itinerary(g, history) -> Grid:
    ngrid = Grid.from_value(g.w, g.h, '.')
    for i in range(1, len(history)-1):
        x, y = history[i]
        x2, y2 = history[i+1]
        if x2-x > 0:
            c = ">"
        elif x2-x < 0:
            c = "<"
        elif y2 - y > 0:
            c = "v"
        else:
            c = "^"
        ngrid[(x, y)] = c

    ngrid[g.s] = "S"
    ngrid[g.e] = "E"
    return ngrid

if __name__ == "__main__":
    input = open(f"d12-sample.txt").read()
    # input = open(f"d12.txt").read()
    g = CustomGrid.from_input(input)
    print(g)
    distances, prev = dijkstra(g, g.s)
    history = build_itinerary(prev, g.s, g.e)
    # print(len(history))
    ngrid = build_debug_itinerary(g, history)
    print(ngrid)
    print(f"part1: {distances[g.e]}")
    # print(len(g.all_As))

    # part2
    a_distance = []
    for a in g.all_As:
        dist, prev = dijkstra(g, a, g.e)
        if g.e in dist:
            a_distance.append(dist[g.e])
    print(f"part2: {min(a_distance)}")
