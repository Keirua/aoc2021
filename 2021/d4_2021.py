import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(4, 2021))

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

class Grid:
    def __init__(self, w, h, value):
        self.lines = []
        for j in range(h):
            curr_line = []
            for i in range(w):
                curr_line.append(value)
            self.lines.append(curr_line)

    def set(self, x, y, v):
        self.lines[y][x] = v

    def get(self, x, y):
        return self.lines[y][x]

    def __repr__(self):
        s = ""
        for l in self.lines:
            s += " ".join(map(str,l)) + "\n"
        return s

class BingoGrid(Grid):
    def __init__(self, grid_as_list):
        super().__init__(5,5,0)
        for y in range(5):
            line = list(map(int, re.findall(r"(\d+)", grid_as_list[y])))
            for x in range(5):
                self.set(x, y, line[x])
    def play(self, v):
        for x in range(5):
            for y in range(5):
                if self.get(x, y) == v:
                    self.set(x, y, None)
    def is_won(self):
        for line in self.lines:
            if any(line) == False:
                return True
        for x in range(5):
            col = [line[x] for line in self.lines]
            if any(col) == False:
                return True
        return False
    def score(self):
        non_nil_values = []
        for x in range(5):
            for y in range(5):
                if self.get(x, y) is not None:
                    non_nil_values.append(self.get(x,y))
        return sum(non_nil_values)



def parse(input):
    lines = aoc.as_lines(input)
    drawns = list(map(int, lines[0].split(",")))
    grids = [BingoGrid(lines[i:i+5]) for i in range(2, len(lines), 6)]
    return drawns, grids

def part1(drawns, grids):
    for d in drawns:
        for g in grids:
            g.play(d)
            if g.is_won():
                return g.score()*d
from collections import deque
def part2(drawns, grids):
    drawns = deque(drawns)
    d = None
    last_grid = None
    while len(grids) > 0:
        d = drawns.popleft()
        remaining_gs = []
        for g in grids:
            g.play(d)
            if not g.is_won():
                remaining_gs.append(g)
            else:
                last_grid = g
        grids = remaining_gs
    return last_grid.score()*d

test_drawns, test_grids = parse(test_input)
drawns, grids = parse(input)
assert(part1(test_drawns, test_grids) == 4512)
test_drawns, test_grids = parse(test_input)
drawns, grids = parse(input)
assert(part2(test_drawns, test_grids) == 1924)
print(part1(drawns, grids))
print(part2(drawns, grids))

