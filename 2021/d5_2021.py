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
@dataclass()
class Line:
    p0: Point
    p1: Point

    def is_v(self): return self.p0.x == self.p1.x
    def is_h(self): return self.p0.y == self.p1.y
    def is_diag(self): return abs(self.p0.y-self.p1.y) == abs(self.p1.x - self.p0.x)

    def all_h_or_v_points(self):
        if self.is_v():
            min_y = min(self.p0.y, self.p1.y)
            max_y = max(self.p0.y, self.p1.y)
            return set([(self.p0.x, y) for y in range(min_y, max_y + 1)])
        if self.is_h():
            min_x = min(self.p0.x, self.p1.x)
            max_x = max(self.p0.x, self.p1.x)
            return set([(x, self.p0.y) for x in range(min_x, max_x + 1)])
        if self.is_diag():
            nb_points = abs(self.p1.y - self.p0.y)
            dx = (self.p1.x - self.p0.x)/nb_points
            dy = (self.p1.y - self.p0.y)/nb_points
            return set([(int(self.p0.x+delta*dx), int(self.p0.y+delta*dy)) for delta in range(nb_points+1)])
        raise ValueError("Impossibru!")

def parse(input):
    ints = list(map(int, re.findall("\d+", input)))
    lines = []
    for i in range(0, len(ints), 4):
        p0 = Point(ints[i+0], ints[i+1])
        p1 = Point(ints[i+2], ints[i+3])
        lines.append(Line(p0, p1))
    return lines

def count_intersections(lines):
    all_coords = set()
    overlapping = set()
    for l in lines:
        for c in l.all_h_or_v_points():
            if c in all_coords:
                overlapping.add(c)
            else:
                all_coords.add(c)
    return len(overlapping)

def part1(lines):
    h_or_v_lines = [line for line in lines if line.is_v() or line.is_h()]
    return count_intersections(h_or_v_lines)


def part2(lines):
    h_or_v_or_diag = [line for line in lines if line.is_v() or line.is_h() or line.is_diag()]
    return count_intersections(h_or_v_or_diag)

sample_line = Line(Point(9,7), Point(7,7))
assert(sample_line.all_h_or_v_points() == set([(7,7), (8, 7), (9,7)]))
sample_line_diag = Line(Point(9,7), Point(7,9))
assert(sample_line_diag.all_h_or_v_points() == set([(9,7), (8, 8), (7,9)]))

assert(part1(parse(test_input)) == 5)
assert(part2(parse(test_input)) == 12)
lines = parse(input)
print(part1(lines))
print(part2(lines))