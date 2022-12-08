import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)
from grid import *
input = open(f"d8.txt").read()
lines = input.split("\n")

class TreeGrid(Grid):
    @classmethod
    def from_lines(cls, lines):
        lines = [[int(v) for v in l] for l in lines]
        return cls(len(lines[0]), len(lines), lines)

    def all_neighbours_in_dir(self, x, y, dx, dy):
        cx, cy = (x+dx, y+dy)
        values = []
        while self.is_in_grid([cx, cy]):
            values.append(self.get(cx, cy))
            cx += dx
            cy += dy
        return values

t = TreeGrid.from_lines(lines)

def rmax(v):
    if len(v) == 0:
        return -1
    return max(v)

nb  = 0
for (x, y) in t.all_coords():
    left = rmax(t.all_neighbours_in_dir(x, y, -1, 0))
    right = rmax(t.all_neighbours_in_dir(x, y, 1, 0))
    top = rmax(t.all_neighbours_in_dir(x, y, 0, 1))
    down = rmax(t.all_neighbours_in_dir(x, y, 0, -1))
    v = t.get(x, y)
    nb += any([v > u for u in [left, right, top, down]])

print(nb)

