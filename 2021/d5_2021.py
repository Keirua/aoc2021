import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(5, 2021))
test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

from dataclasses import dataclass
@dataclass()
class Point:
    x: int
    y: int

def parse(input):
    ints = list(map(int, re.findall("\d+", input)))
    lines = []
    for i in range(0, len(ints), 4):
        p0 = Point(ints[i+0], i+1)
        p1 = Point(ints[i+2], i+3)
        lines.append((p0, p1))
    return lines

lines = parse(input)
test_lines = parse(test_input)
pp.pprint(lines)
print()
pp.pprint(test_lines)
