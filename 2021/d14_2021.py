import aoc
import re, pprint, itertools as it
from collections import Counter

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
    new_pairs = {}
    replacement = {}
    new_letter = {}
    for k, v in re.findall(r"(.*) -> (.*)", input):
        new_pairs[k] = [f"{k[0]}{v}", f"{v}{k[1]}"]
        new_letter[k] = v
        replacement[k] = f"{v}{k[1]}"

    return input[:input.find("\n")], new_pairs, replacement, new_letter


def step(template, rules):
    res = str(template[0])
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        assert (pair in rules.keys())
        res += rules[pair]
    return res


def part1(template, rules, n=5):
    """naive implementation, doesnt scale fast past n = 15 due to growth that follows fibonacci"""
    for i in range(1, n + 1):
        template = step(template, rules)
    c = Counter(list(template))
    return max(c.values()) - min(c.values())


def part2(template, rules, new_letters, n=5):
    letters_count = Counter(list(template))
    pair_count = Counter([template[i:i + 2] for i in range(len(template) - 1)])

    for i in range(1, n + 1):
        new_pair_count = Counter()
        for p in pair_count.keys():
            # So each pair creates 2 pair and creates one new letter
            pair_a, pair_b = rules[p]
            new_letter = new_letters[p]
            # all we have to do is keep track of the letter counts and the pair counts
            letters_count[new_letter] += pair_count[p]
            new_pair_count[pair_a] += pair_count[p]
            new_pair_count[pair_b] += pair_count[p]
        pair_count = new_pair_count

    return max(letters_count.values()) - min(letters_count.values())


test_template, test_rules, test_replacements, test_new_letter = parse(test_input)
template, rules, replacements, new_letter = parse(input)

assert (part1(test_template, test_replacements, 10) == 1588)
print(part1(template, replacements, 10))
assert (part2(test_template, test_rules, test_new_letter, 10) == 1588)
assert (part2(test_template, test_rules, test_new_letter, 40) == 2188189693529)
print(part2(template, rules, new_letter, 40))
