from aoc import input_as_string, challenge_filename
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = input_as_string(challenge_filename(12, 2021))
test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
test_input2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

def parse(input):
    edges = {}
    lines = input.split("\n")
    for line in lines:
        a, b = line.split("-")
        if a not in edges:
            edges[a] = []
        if b not in edges:
            edges[b] = []
        edges[a].append(b)
        edges[b].append(a)
    return edges

# edges = {
#     "a": ["b", "c"], # from a, it is possible to go to b or c
#     "b": ["d", "e"],
#     "c": ["f", "g"],
#     "d": [],
#     "e": ["h"],
#     "f": [],
#     "g": []
# }

test_graph = parse(test_input)
pp.pprint(test_graph)
