import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(2, 2015))
lines = aoc.as_lines(input)

total = 0
for l in lines:
    dims = list(map(int, l.rstrip("\n").split("x")))
    sides = [x*y for x, y in it.combinations(dims, 2)]
    total += 2*sum(sides) + min(sides)

pp.pprint(total)
