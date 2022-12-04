import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

#input = open("d4-sample.txt")
input = open("d4.txt")

lines = [l.strip() for l in input]

pp.pprint(lines)
