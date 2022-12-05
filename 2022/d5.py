import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open("d5.txt").readlines()
lines = [l.strip("\n") for l in input]

pp.pprint(lines)
