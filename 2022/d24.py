import pprint as pp, itertools as it
from collections import Counter

DELTAS = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
    "^": (0, -1),
}

class Grid:
    def __init__(self, lines):
        self.blizzards = []
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

    def next_blizzards(self, blizzards):
        next_blizz = []
        for (x, y, c) in blizzards:
            dx, dy = DELTAS[c]
            nx, ny = x+dx, y+dy
            if c == ">" and nx == self.W-1:
                nx = 1
            if c == "v" and ny == self.H-1:
                ny = 1
            if c == "<" and nx == 0:
                nx = self.W-2
            if c == "^" and ny == 0:
                ny = self.H-2
            next_blizz.append((nx, ny, c))
        return next_blizz

    def print_grid(self):
        out = [["." for _ in range(self.W)] for _ in range(self.H)]
        for x in range(self.W):
            out[0][x] = "#"
            out[-1][x] = "#"
        for y in range(self.H):
            out[y][0] = "#"
            out[y][-1] = "#"
        out[self.start_y][self.start_x] = 'S'
        out[self.end_y][self.end_x] = 'E'
        counter = Counter([(x, y) for (x, y, c) in self.blizzards])
        for (x, y, c) in self.blizzards:
            if counter[(x, y)] == 1:
                out[y][x] = c
        for (x, y), v in counter.items():
            if v > 1:
                out[y][x] = str(v)

        return "\n".join(["".join(l) for l in out])


lines = open(f"d24.txt").read().strip().splitlines()
lines = open(f"d24-sample.txt").read().strip().splitlines()
lines = open(f"d24-sample2.txt").read().strip().splitlines()
g = Grid(lines)
pp.pprint(g.blizzards)
for i in range(10):
    print(g.print_grid())
    g.blizzards = g.next_blizzards(g.blizzards)
    # print(g.blizzards)
    print()
# pp.pprint(lines)
