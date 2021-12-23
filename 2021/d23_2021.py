import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(23, 2021))
def parse(input):
    map = aoc.as_lines(input)
    positions = {k:[] for k in "ABCD"}
    for j, line in enumerate(map):
        for i, cell in enumerate(line):
            if cell in "ABCD":
                positions[cell].append((i,j))
    return map, positions

map, positions = parse(input)
pp.pprint(positions)
pp.pprint(map)
