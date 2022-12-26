import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

lines = open(f"d24.txt").read().strip().splitlines()
lines = open(f"d24-sample.txt").read().strip().splitlines()

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

        return "\n".join(["".join(l) for l in lines])



g = Grid(lines)
pp.pprint(g.blizzards)
print(g.print_grid())
# pp.pprint(lines)
