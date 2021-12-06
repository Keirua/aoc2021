import aoc
import re, pprint, itertools as it
from collections import Counter
from functools import partial
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(6, 2021))
test_input = "3,4,3,1,2"
def parse(input):
    return list(map(int,re.findall("\d+", input)))

ints = parse(input)
test_ints = parse(test_input)

def update_population_count(c):
    c2 = Counter()
    for i in range(1, 8+1):
        c2[i-1] = c[i]
    c2[6] += c[0]
    c2[8] += c[0]
    return c2

def count_population(ints, n=80):
    c = Counter(ints)
    for i in range(n):
        c = update_population_count(c)
    return sum(c.values())

if __name__ == "__main__":
    part1 = partial(count_population, n=80)
    part2 = partial(count_population, n=256)

    assert(count_population(test_ints, 18) == 26)
    assert(count_population(test_ints, 80) == 5934)
    assert(part2(test_ints) == 26984457539)

    print(part1(ints))
    print(part2(ints))
