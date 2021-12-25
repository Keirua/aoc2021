import aoc
import re, pprint, itertools as it
from dataclasses import dataclass

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(25, 2021))
test_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""


@dataclass
class Grid:
    map: list
    w: int
    h: int

    def __str__(self):
        o = ""
        for y in range(self.h):
            o += "".join(self.map[y]) + "\n"
        return o


def parse(input: str) -> Grid:
    lines = aoc.as_lines(input)
    map = [list(l.rstrip()) for l in lines]
    return Grid(map, len(map[0]), len(map))


def step(g: Grid):
    moved = False
    # We create an empty map
    map2 = [["." for _ in range(g.w)] for _ in range(g.h)]
    # first, all the east-facing sea cucumbers try to move east
    for y in range(g.h):
        for x in range(g.w):
            nx = (x + 1) % g.w
            if g.map[y][x] == ">":
                if g.map[y][nx] == ".":
                    map2[y][nx] = ">"
                    moved = True
                else:
                    map2[y][x] = ">"
    # Then, the south-facing herd attempt to move
    for x in range(g.w):
        for y in range(g.h):
            if g.map[y][x] == "v":
                ny = (y + 1) % g.h
                if map2[ny][x] == "." and g.map[ny][x] != "v":
                    map2[ny][x] = "v"
                    moved = True
                else:
                    map2[y][x] = "v"

    return Grid(map2, g.w, g.h), moved


def part1(grid):
    nb_steps = 0
    while True:
        grid, moved = step(grid)
        nb_steps += 1
        if not moved:
            return nb_steps


grid = parse(input)
test_grid = parse(test_input)
assert (part1(test_grid) == 58)
print(part1(grid))
