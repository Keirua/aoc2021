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

    def all_h_or_v_points(self):
        if self.is_v():
            min_y = min(self.p0.y, self.p1.y)
            max_y = max(self.p0.y, self.p1.y)
            return set([(self.p0.x, y) for y in range(min_y, max_y + 1)])
        if self.is_h():
            min_x = min(self.p0.x, self.p1.x)
            max_x = max(self.p0.x, self.p1.x)
            return set([(x, self.p0.y) for x in range(min_x, max_x + 1)])
        raise ValueError("Impossibru!")

def parse(input):
    ints = list(map(int, re.findall("\d+", input)))
    lines = []
    for i in range(0, len(ints), 4):
        p0 = Point(ints[i+0], ints[i+1])
        p1 = Point(ints[i+2], ints[i+3])
        lines.append(Line(p0, p1))
    return lines

def part1_v2(input):
    lines = parse(input)
    h_or_v_lines = [line for line in lines if line.is_v() or line.is_h()]
    all_coords = []
    overlapping = []
    for l in h_or_v_lines:
        for c in l.all_h_or_v_points():
            if not c in all_coords:
                all_coords.append(c)
            else:
                overlapping.append(c)
    return len(set(overlapping))

def part1_v3(input):
    lines = parse(input)
    h_or_v_lines = [line for line in lines if line.is_v() or line.is_h()]
    all_coords = set()
    overlapping = set()
    for l in h_or_v_lines:
        for c in l.all_h_or_v_points():
            if c in all_coords:
                overlapping.add(c)
            else:
                all_coords.add(c)
    return len(overlapping)

def part1_v1(input):
    lines = parse(input)
    pp.pprint(lines)
    h_or_v_lines = [line for line in lines if line.is_v() or line.is_h()]

    all_intersection_points = set()
    for i in range(0, len(h_or_v_lines)):
        for j in range(0, len(h_or_v_lines)):
            if i == j:
                continue
            pa = h_or_v_lines[i].all_h_or_v_points()
            pb = h_or_v_lines[j].all_h_or_v_points()
            all_intersection_points |= pa&pb
    return len(set(all_intersection_points))

part1 = part1_v3
# sample_line = Line(Point(9,7), Point(7,7))
# assert(sample_line.all_h_or_v_points() == set([(7,7), (8, 7), (9,7)]))

# assert(part1(test_input) == 5)
# # 5744 to low, 6544 is too high
print(part1(input))