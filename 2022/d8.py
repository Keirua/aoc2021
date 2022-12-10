import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)
from grid import *


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


def rmax(v):
    if len(v) == 0:
        return -1
    return max(v)

def part1(t):
    nb = 0
    for (x, y) in t.all_coords():
        left = rmax(t.all_neighbours_in_dir(x, y, -1, 0))
        right = rmax(t.all_neighbours_in_dir(x, y, 1, 0))
        top = rmax(t.all_neighbours_in_dir(x, y, 0, 1))
        down = rmax(t.all_neighbours_in_dir(x, y, 0, -1))
        v = t.get(x, y)
        nb += any([v > u for u in [left, right, top, down]])
    return nb

def nb_vis(neighbours, v):
    nb = 1
    for n in neighbours:
        if n >= v:
            return nb
        else:
            nb += 1
    return len(neighbours)
import math
def part2(t):
    nb = 0
    for (x, y) in t.all_coords():
        left = t.all_neighbours_in_dir(x, y, -1, 0)
        right = t.all_neighbours_in_dir(x, y, 1, 0)
        top = t.all_neighbours_in_dir(x, y, 0, 1)
        down = t.all_neighbours_in_dir(x, y, 0, -1)
        v = t.get(x, y)

        curr = math.prod([nb_vis(u, v) for u in [left, right, top, down]])
        nb = max(curr, nb)
    return nb

input = open(f"d8.txt").read()
lines = input.split("\n")
t = TreeGrid.from_lines(lines)
# print(part1(t))
print(part2(t))

