import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(9, 2015))
def parse(input):
    lines = re.findall(r"(.*) to (.*) = (\d+)", input)
    cities = set()
    distances = {}
    for a, b, distance in lines:
        cities |= set([a, b])
    for c in cities:
        distances[c] = {}
        for c2 in cities:
            distances[c][c2] = 0
    for a, b, d in lines:
        distances[a][b] = int(d)
        distances[b][a] = int(d)
    return cities, distances

test_input = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

cities, distances = parse(input)
cities, distances = parse(test_input)
pp.pprint(distances)
def compute_distance(itinerary, distances):
    return sum([distances[itinerary[i]][itinerary[i+1]] for i in range(len(itinerary)-1)])

min_dist = 1000000000000
max_dist = 0
for p in it.permutations(cities):
    d = compute_distance(p, distances)
    if d < min_dist:
        min_dist = d
    if d > max_dist:
        max_dist = d
print(min_dist)
print(max_dist)