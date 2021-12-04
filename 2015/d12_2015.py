import aoc
import re, pprint
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(12, 2015))

def part1(input):
    """Finding all the integers is solved with a regex"""
    ints = map(int, re.findall(r"(-?\d+)", input))
    return sum(ints)

print(part1(input))
import json
import copy
o = json.loads(input)
def bfs(o):
    if type(o) == list:
        for v in o:
            bfs(v)
        return o
    else:
        src = copy.deepcopy(o)
        if "red" in o.values():
            for k in o.keys():
                del src[k]
        o = src
        return o





test_input = """{"d":"red","e":[1,2,3,4],"f":5}"""
test_input2 = """[1,{"c":"red","b":2},3]"""
# o = json.loads(test_input)
o = json.loads(test_input2)
o = bfs(o)
# pp.pprint(o)
# print(o.keys())
pp.pprint(o)
# print(part1(input))

