import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

lines = open(f"d3.txt").read().splitlines()
p1 = 0
for l in lines:
    a,b,c = [int(i) for i in re.findall(r"(\d+)", l)]
    p1 += (a+b > c) and (a+c) > b and (b+c) > a
pp.pprint(p1)
