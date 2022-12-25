import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open(f"d25.txt").read()
input = open(f"d25-sample.txt").read()
lines = input.split("\n")

def sctoi(c):
    try:
        return int(c)
    except:
        if c == "-":
            return -1
        if c == "=":
            return -2

def snafu_to_i(s):
    out = 0
    coef = 1
    for c in s[::-1]:
        out += sctoi(c)*coef
        coef *= 5
    return out

print(sum(map(snafu_to_i, lines)))

# pp.pprint(lines)
