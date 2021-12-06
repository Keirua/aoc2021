import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(6, 2021))
test_input = "3,4,3,1,2"
def parse(input):
    return list(map(int,re.findall("\d+", input)))

ints = parse(input)
test_ints = parse(test_input)

def step(ints):
    new_ints = []
    for i in ints:
        if i>0:
            new_ints.append(i-1)
        else:
            new_ints.append(6)
            new_ints.append(8)
    return new_ints

def part1(ints, n=80):
    for i in range(n):
        ints = step(ints)
    return len(ints)

pp.pprint(test_ints)
assert(part1(test_ints, 18) == 26)
assert(part1(test_ints, 80) == 5934)

pp.pprint(part1(ints, 80))
# pp.pprint(ints)
