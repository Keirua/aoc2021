import aoc
import re, pprint, itertools as it
from collections import Counter
pp = pprint.PrettyPrinter(indent=4)

def parse(input):
    positions = aoc.all_ints(input)
    return Counter(positions)

input = aoc.input_as_string(aoc.challenge_filename(7, 2021))
test_input = "16,1,2,0,4,2,7,1,2,14"

positions = parse(input)
test_positions = parse(test_input)
def score(positions, align_at):
    s = 0
    for k in positions.keys():
        s += abs(align_at - k) * positions[k]
    return s

def part1(positions):
    # all we have to do is minimize the score, and in order to do that the crabs have to go towards the center,
    # so between the min and max value.
    # so we compute the cost of movement for each position over this range
    return min(score(positions, i) for i in range(min(positions.keys()), max(positions.keys())+1))

assert(score(test_positions, 1) == 41)
assert(score(test_positions, 3) == 39)
assert(score(test_positions, 10) == 71)
assert(part1(test_positions) == 37)
print(part1(positions)) # max - min = 1904
