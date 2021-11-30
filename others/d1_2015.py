#!/usr/bin/python3
import aoc

import itertools as it
import pprint
import re
pp = pprint.PrettyPrinter(indent=4)

filename = aoc.challenge_filename(1, 2015)
input = aoc.input_as_string(filename)

from collections import Counter
# floors = Counter(input)
# f = floors['(']-floors['(']
f = 0
first_minus_1 = None
for i,c in enumerate(input):
	if c=='(':
		f += 1
	elif c==')':
		f -= 1
	if f == -1 and first_minus_1 is None:
		first_minus_1 = i+1
print(f, first_minus_1)