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

def parse(input):
    lines = aoc.as_lines(input)
    grid = [list(l.rstrip()) for l in lines]
    w, h = len(grid[0]), len(grid)
    return Grid(grid, w, h)

def step(g:Grid):
    grid2 = [["." for _ in range(g.w)] for _ in range(g.h)]
    # first, the east-facing sea cucumbers try to move east
    for y in range(g.h):
        for x in range(g.w):
            if x+1 < g.w:
                pass
    return Grid(grid2, g.w, g.h)

grid = parse(input)
test_grid = parse(test_input)
grid2 = step(test_grid)
print(test_grid)
print(grid2)
