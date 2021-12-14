import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(14, 2021))
test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

def parse(input):
    lines = aoc.as_lines(input)
    rules = {}
    replacement = {}
    for line in lines[2:]:
        k,v = line.strip().split(" -> ")
        k = k.strip()
        v = v.strip()
        rules[k] = v
        replacement[k] = f"{v}{k[1]}"

    return lines[0].strip(), rules, replacement

def step(template, rules):
    res = str(template[0])
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair in rules.keys():
            res += rules[pair]
    return res

from collections import Counter
def score(template):
    c = Counter(list(template))
    return max(c.values()) - min(c.values())

def part1(template, rules, n=5):
    for i in range(1, n+1):
        template = step(template, rules)
    return score(template)

def part2(template, rules, n=5):
    for i in range(1, n+1):
        template = step(template, rules)
        print(i)
    return score(template)



test_template, test_rules, test_replacements = parse(test_input)
template, rules, replacements = parse(input)

# print(test_template, test_replacements)
assert(part1(test_template, test_replacements, 10) == 1588)
print(part1(template, replacements, 10))
print(part2(template, replacements, 40))
# print(template, replacements)
# pp.pprint(lines)
