#!/usr/bin/python3
import aoc

from itertools import product
import re
# re.findall(expr, s) | Matches all instances of an expression A in a string B and returns them in a list.
# re.search(expr, s) | Matches the first instance of an expression A in a string B, and returns it as a re match object.
# re.split(expr, s) | Split a string B into a list using the delimiter A.
# re.sub(A, B, C) | Replace A with B in the string C.
import pprint
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint([1,2,3])


filename = aoc.challenge_filename(1, 2020)
s = aoc.input_as_string(filename)
print(s)
lines = aoc.input_as_lines(filename)

print(lines)
lines = aoc.input_as_ints(filename)

print(lines)

# for a, b in product(lines, lines):
# 	if a + b == 2020:
# 		part1 = a * b

# for a, b, c in product(lines, lines, lines):
# 	if a + b + c == 2020:
# 		part2 = a * b * c

# print(part1)
# print(part2)

# Splitting according to a somewhat complex pattern (2016, day 7)
# re.split(r'\[|\]', "abc[def]ghi") # returns ['abc', 'def', 'ghi']

# Sometimes, you don’t have to split. You can look for the useful part with a regex right away
# Finding numbers
s = "123, 4, 56, 789"
list_as_str = re.findall(r'(\d+)', s) #
print(list_as_str) # ['123', '4', '56', '789']
array = list(map(int, list_as_str))
# or if you prefer list comprehensions:
array = [int(n) for n in list_as_str]
pp.pprint(array) # [123, 4, 56, 789]

# Finding movements (2017, day 7)
s = "N12, S1, W4"
matches = re.findall(r'([NSEW])(\d+)', s)
pp.pprint(matches) # [('N', '12'), ('S', '1'), ('W', '4')]

# 2018, day 7:
# Step A must be finished before step N can begin.
# Step P must be finished before step R can begin.
# Step O must be finished before step T can begin.
# …
s = """Step A must be finished before step N can begin.
Step P must be finished before step R can begin.
Step O must be finished before step T can begin."""
data = re.findall("Step (.*) must be finished before step (.*) can begin.", s)
print(data) # [('A', 'N'), ('P', 'R'), ('O', 'T')]


# pp.pprint(array)
# https://gto76.github.io/python-cheatsheet/



# https://github.com/norvig/pytudes/blob/main/ipynb/Advent%20of%20Code.ipynb
from collections import Counter, defaultdict, namedtuple, deque
from functools   import lru_cache
from itertools   import permutations, combinations, chain, cycle, product, islice
from heapq       import heappop, heappush