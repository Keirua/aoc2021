import re
from z3 import *

def parse(text):
    return [list(map(int, re.findall("(-?\d+)", l))) for l in text.strip().split("\n")]

def manhattan_distance(x, y, x2, y2):
    """https://en.wikipedia.org/wiki/Taxicab_geometry"""
    return abs(x2 - x) + abs(y2 - y)

def find_impossible(positions, y0=2000000):
    not_possible = set()
    for (x, y, x2, y2) in positions:
        dist = manhattan_distance(x, y, x2, y2)
        dx = dist - abs(y0-y)
        if dx < 0:
            continue
        for curr_x in range(dx+1):
            if (x+curr_x, y0) != (x2, y2):
                not_possible.add(x+curr_x)
            if (x-curr_x, y0) != (x2, y2):
                not_possible.add(x-curr_x)
    return set(not_possible)

def part1(positions, y0=2000000):
    return len(find_impossible(positions, y0))

def z3Abs(v):
    # no abs in z3, and abs from python’s builtin does not work with ArithRef
    return If(v>0, v, -v)

def part2(positions, xy_max):
    solver = Solver()
    tx, ty, p2 = Ints("x y p2")
    solver.add(And(tx >= 0, tx <= xy_max))
    solver.add(And(ty >= 0, ty <= xy_max))
    solver.add(p2 == tx*4000000+ty)
    for (x, y, x2, y2) in positions:
        dist = manhattan_distance(x, y, x2, y2)
        solver.add(z3Abs(x-tx)+z3Abs(y - ty) > dist)
    solver.check()
    m = solver.model()
    return m[p2]

text_sample = open(f"d15-sample.txt").read()
d15_pos_sample = parse(text_sample)
text = open(f"d15.txt").read()
d15_pos = parse(text)

assert(part1(d15_pos_sample, 10) == 26)
assert(part2(d15_pos_sample, 20) == 56000011)
print(part1(d15_pos))
print(part2(d15_pos, 4000000))
