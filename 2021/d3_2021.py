import aoc
from functools import partial

input = aoc.input_as_string(aoc.challenge_filename(3, 2021))
test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
lines = aoc.as_lines(input)
test_lines = aoc.as_lines(test_input)

from collections import Counter

def gamma(c): return "1" if c["0"] > c["1"] else "0"
def epsilon(c): return "1" if c["0"] < c["1"] else "0"
cmp_oxygen = lambda c: "1" if c["1"] >= c["0"] else "0"
cmp_co2 = lambda c: "0" if c["0"] <= c["1"] else "1"

# def to_int(b):
#     """Converts a binary string (base 2, like 010011) to a base 10 integer (19)"""
#     nb = 0
#     l = len(b)
#     p = 1
#     for i in range(l):
#         nb += p * int(b[l-i-1])
#         p*=2
#     return nb
# Ok so I spent way too much time implementing this when it’s the demo example for partial…
# https://docs.python.org/3/library/functools.html#functools.partial
to_int = partial(int, base=2)

def part1(lines):
    bin_gamma = ""
    bin_epsilon = ""
    for i in range(len(lines[0])):
        digits = [l[i] for l in lines]
        c = Counter(digits)
        bin_gamma += gamma(c)
        bin_epsilon += epsilon(c)
    return to_int(bin_epsilon)*to_int(bin_gamma)

def bit_criteria(cmp, lines, pos):
    digits = [l[pos] for l in lines]
    c = Counter(digits)
    return cmp(c)

bit_criteria_oxygen = partial(bit_criteria, cmp_oxygen)
bit_criteria_co2 = partial(bit_criteria, cmp_co2)

def filter_by_bit_criteria(lines, p, bit_criteria):
    return list(filter(lambda line: line[p] == bit_criteria, lines))

def find_one_by_criteria(lines, bit_criteria_cb):
    remaining = lines
    p = 0
    while len(remaining) > 1:
        bc = bit_criteria_cb(remaining, p)
        remaining = filter_by_bit_criteria(remaining, p, bc)
        p += 1
    return remaining[0]

find_oxygen = partial(find_one_by_criteria, bit_criteria_cb=bit_criteria_oxygen)
find_co2 = partial(find_one_by_criteria, bit_criteria_cb=bit_criteria_co2)
# same as:
# def find_oxygen(lines): return find_by_criteria(lines, bit_criteria_oxygen)
# def find_co2(lines): return find_by_criteria(lines, bit_criteria_co2)

def part2(lines): return to_int(find_oxygen(lines)) * to_int(find_co2(lines))

print(part1(test_lines))
print(part1(lines))

print(part2(test_lines))
print(part2(lines))

