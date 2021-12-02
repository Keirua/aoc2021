import aoc
import itertools as it
import pprint
import re
pp = pprint.PrettyPrinter(indent=4)

test_input = """ULL
RRDDD
LURDL
UUUUD"""

input = aoc.input_as_string(aoc.challenge_filename(2, 2016))
# input = test_input
mapping = {
    'L': (-1, 0),
    'R': (1, 0),
    'D': (0, 1),
    'U': (0, -1),
}
lines = aoc.as_lines(input)

code = [
    "    ",
    " 123 ",
    " 456 ",
    " 789 ",
    "     ",
]

code2 = [
    "       ",
    "   1   ",
    "  234  ",
    " 56789 ",
    "  ABC  ",
    "   D   ",
    "       ",
]
def find_password(instructions, code, x, y):
    password = ""
    for line in lines:
        for i in line:
            assert(i in mapping.keys())
            movement = mapping[i]
            nx = x + movement[0]
            ny = y + movement[1]
            if code[ny][nx] != " ":
                x, y = nx, ny

        password += code[y][x]
    return password

part1 = find_password(lines, code, 1, 1)
part2 = find_password(lines, code2, 1, 3)
print(part1)
print(part2)
