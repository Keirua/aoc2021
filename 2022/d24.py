import pprint as pp, itertools as it
from collections import Counter, defaultdict
from heapq import heappop, heappush

DELTAS = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
    "^": (0, -1),
}


class Grid:
    def __init__(self, lines):
        self.blizzards = []
        self.walls = []
        self.movable = []
        self.W = len(lines[0])
        self.H = len(lines)
        self.start_x = lines[0].index('.')
        self.start_y = 0
        self.end_x = lines[-1].index('.')
        self.end_y = self.H - 1
        for j, l in enumerate(lines):
            for i, c in enumerate(l):
                if c in "<>^v":
                    self.blizzards.append((i, j, c))
                if c == "#":
                    self.walls.append((i, j))
                else:
                    self.movable.append((i, j))
        self.KNOWN_BLIZZARDS = {}

    def next_blizzards(self, blizzards):
        next_blizz = []
        for (x, y, c) in blizzards:
            dx, dy = DELTAS[c]
            nx, ny = x + dx, y + dy
            if c == ">" and nx == self.W - 1:
                nx = 1
            if c == "v" and ny == self.H - 1:
                ny = 1
            if c == "<" and nx == 0:
                nx = self.W - 2
            if c == "^" and ny == 0:
                ny = self.H - 2
            next_blizz.append((nx, ny, c))
        return next_blizz

    # def print_grid(self, blizzards):
    #     out = [["." for _ in range(self.W)] for _ in range(self.H)]
    #     for (x, y) in self.walls:
    #         out[y][x] = "#"
    #     out[self.start_y][self.start_x] = 'S'
    #     out[self.end_y][self.end_x] = 'E'
    #     counter = Counter([(x, y) for (x, y, c) in blizzards])
    #     for (x, y, c) in blizzards:
    #         if counter[(x, y)] == 1:
    #             out[y][x] = c
    #     for (x, y), v in counter.items():
    #         if v > 1:
    #             out[y][x] = str(v)
    #
    #     return "\n".join(["".join(l) for l in out])

    def dbg(self, blizzards, sx, sy):
        out = [["." for _ in range(self.W)] for _ in range(self.H)]
        for (x, y) in self.walls:
            out[y][x] = "#"
        counter = Counter([(x, y) for (x, y, c) in blizzards])
        for (x, y, c) in blizzards:
            if counter[(x, y)] == 1:
                out[y][x] = c
        for (x, y), v in counter.items():
            if v > 1:
                out[y][x] = str(v)
        out[sy][sx] = "E"

        return "\n".join(["".join(l) for l in out])


    def get_blizzard_at(self, t):
        if t in self.KNOWN_BLIZZARDS:
            return self.KNOWN_BLIZZARDS[t]
        blizz = self.blizzards
        while t > 0:
            blizz = self.next_blizzards(blizz)
            t -= 1
        self.KNOWN_BLIZZARDS[t] = blizz
        return blizz

    def solve(self):
        """
        Dijkstra in moving map
        """
        Q = [(0, 0, (self.start_x, self.start_y))]
        DIST = {(x, y, 0): 1000000000000000 for (x, y) in self.movable}
        DIST[(g.start_x, g.start_y, 0)] = 0
        PREV = {(x, y, 0): None for (x, y) in self.movable}
        while len(Q) > 0:
            min_dist, t, (x, y) = heappop(Q)
            if (x, y) == (self.end_x, self.end_y):
                break
            # Do we have a better path already?
            if (x, y, t) in DIST and DIST[(x, y, t)] < min_dist:
                continue
            # Generate the possible next moves (4 cardinal directions + don’t move)
            next_blizzard = self.get_blizzard_at(t + 1)
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
                nx, ny = x + dx, y + dy
                new_dist = DIST[(x, y, t)] + 1
                if 0 <= nx <= self.W-1 and 0<= ny <= self.H-1 and (nx, ny) not in self.walls and (nx, ny) not in next_blizzard:
                    if (nx, ny, t + 1) not in DIST or DIST[(nx, ny, t + 1)] > new_dist:
                        DIST[(nx, ny, t + 1)] = new_dist
                        PREV[(nx, ny, t + 1)] = (x, y)
                        heappush(Q, (new_dist, t + 1, (nx, ny)))

        return t, PREV


def find_history(prev, t):
    history = [(g.end_x, g.end_y)]
    parent = prev[(g.end_x, g.end_y, t)]
    while parent is not None:
        history.append(parent)
        (x, y) = parent
        parent = prev[(x, y, t-1)]
        t -= 1
    return history[::-1]

lines = open(f"d24.txt").read().strip().splitlines()
lines = open(f"d24-sample.txt").read().strip().splitlines()
# lines = open(f"d24-sample2.txt").read().strip().splitlines()
g = Grid(lines)
# pp.pprint(g.blizzards)
t, prev = g.solve()
print(t)

history = find_history(prev, t)
for t, h in enumerate(history):
    x, y = h
    # print(g.dbg(g.get_blizzard_at(t), g.start_x, g.start_y))
    print(g.dbg(g.get_blizzard_at(t+1), x, y))
    print()
