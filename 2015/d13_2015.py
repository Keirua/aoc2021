import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(13, 2015))
test_input = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

def parse(input):
    happynesses = re.findall(r"(.*) would (.*) (\d+) happiness units by sitting next to (.*)\.", input)

    students = set()
    for s1, verb, quantity, s2 in happynesses:
        students = students | set([s1, s2])

    mapping = {}
    for s1 in students:
        mapping[s1] = {}
        for s2 in students:
            mapping[s1][s2] = 0
    for s1, verb, quantity, s2 in happynesses:
        q = int(quantity)
        if verb != "gain":
            q = -q
        # s1 would have Q happiness units by sitting next to s2.
        mapping[s1][s2] = q
    return students, mapping

def eval_happyness_change(arrangement, mapping):
    happyness = 0
    for i, a in enumerate(arrangement):
        prev_i = (i-1+len(arrangement)) % len(arrangement)
        next_i = (i+1+len(arrangement)) % len(arrangement)
        happyness += mapping[a][arrangement[prev_i]] + mapping[a][arrangement[next_i]]
    return happyness

students, mapping = parse(test_input)
students, mapping = parse(input)

from itertools import permutations
def part1(students, mapping):
    m = 0
    for p in permutations(students):
        h = eval_happyness_change(p, mapping)
        if h > m:
            m = h
    return m


def part2(students, mapping):
    students = students | set(["me"])
    mapping["me"] = {}
    for s2 in students:
        mapping["me"][s2] = 0
        mapping[s2]["me"] = 0
    return part1(students, mapping)

students, mapping = parse(input)
print(part1(students, mapping))
print(part2(students, mapping))

