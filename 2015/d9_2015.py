import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(9, 2015))
test_input = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""


def parse(input: str) -> dict:
    map = {}
    for l in input.splitlines():
        a, b, cost = re.findall(r"([A-Za-z]+) to ([A-Za-z]+) = (\d+)", l)[0]
        if a not in map:
            map[a] = {}
        if b not in map:
            map[b] = {}
        map[a][b] = int(cost)
        map[b][a] = int(cost)
    return map


def day9(map) -> int:
    cities = map.keys()
    lowest_distance = 999999999
    biggest_distance = 0
    for trip in it.permutations(cities):
        distance = 0
        for i in range(1, len(trip)):
            distance += map[trip[i]][trip[i - 1]]
        if distance < lowest_distance:
            lowest_distance = distance
        if distance > biggest_distance:
            biggest_distance = distance
    return lowest_distance, biggest_distance


pp.pprint(parse(test_input))
assert (day9(parse(test_input)) == (605, 982))
print(day9(parse(input)))
