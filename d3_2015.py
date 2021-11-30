import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(3, 2015))
# lines = aoc.as_lines(input)
mapping = {
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

def count_houses(input):
    x, y = (0, 0)
    houses = [(x, y)]
    for m in input:
        dx, dy = mapping[m]
        x, y = x+dx, y+dy
        houses.append((x,y))

    return len(set(houses))

assert(count_houses(">") == 2)
assert(count_houses("^>v<") == 4)
assert(count_houses("^v^v^v^v^v") == 2)
print(count_houses(input))
