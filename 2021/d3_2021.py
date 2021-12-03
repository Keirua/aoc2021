import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

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
def gamma(c):
    nb_0, nb_1 = c["0"], c["1"]
    if nb_0 < nb_1:
        return "1"
    return "0"

def epsilon(c):
    nb_0, nb_1 = c["0"], c["1"]
    if nb_0 < nb_1:
        return "0"
    return "1"

def to_int(b):
    nb = 0
    l = len(b)
    p = 1
    for i in range(l):
        nb += p * int(b[l-i-1])
        p*=2
    return nb

def part1(lines):
    bin_gamma = ""
    bin_epsilon = ""
    for i in range(len(lines[0])):
        digits = []
        for l in lines:
            digits.append(l[i])
        c = Counter(digits)
        bin_gamma += gamma(c)
        bin_epsilon += epsilon(c)
    return to_int(bin_epsilon)*to_int(bin_gamma)

print(part1(test_lines))
print(part1(lines))

