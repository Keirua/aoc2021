import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(2, 2015))
lines = aoc.as_lines(input)

def part1(lines):
    total = 0
    for l in lines:
        dims = list(map(int, l.rstrip("\n").split("x")))
        sides = [x*y for x, y in it.combinations(dims, 2)]
        total += 2*sum(sides) + min(sides)
    return total

from math import prod
def part2(lines):
    total = 0
    for l in lines:
        dims = list(map(int, l.rstrip("\n").split("x")))
        bow = prod(dims)
        perimeters = [2*(x+y) for x, y in it.combinations(dims, 2)]
        total += bow + min(perimeters)
    return total

pp.pprint(part1(lines))
assert(part2(['2x3x4']) == 34)
assert(part2(['1x1x10']) == 14)
pp.pprint(part2(lines))
