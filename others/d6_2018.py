#!/usr/bin/python3
import aoc

from itertools import product
import re
import pprint
import re
pp = pprint.PrettyPrinter(indent=4)

filename = aoc.challenge_filename(6, 2018)
input = aoc.input_as_string(filename)

coordinates = [(int(x), int(y)) for (x, y) in re.findall(r"(\d+), (\d+)", input)]
print(coordinates)
Xs = [x for (x, y) in coordinates]
Ys = [y for (x, y) in coordinates]
print(min(Xs), max(Xs))
print(min(Ys), max(Ys))