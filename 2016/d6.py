import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)
from collections import Counter
lines = open(f"d6.txt").read().splitlines()
# lines = open(f"d6-sample.txt").read().splitlines()
pw = []
pw2 = []
positions = ["" for i in range(len(lines[0]))]
for l in lines:
    for i,c in enumerate(l):
        positions[i] += c
for p in positions:
    c = Counter(list(p))
    best, _ = c.most_common(1)[0]
    worst, _ = c.most_common(100)[-1]
    pw.append(best)
    pw2.append(worst)

pp.pprint("".join(pw))
pp.pprint("".join(pw2))
