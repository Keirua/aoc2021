import aoc
import re, pprint
pp = pprint.PrettyPrinter(indent=4)

def parse(lines):
    operations = []
    for l in lines:
        op, x1, y1, x2, y2 = re.findall(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", l)[0]
        operations.append([op, (int(x1), int(y1)), (int(x2), int(y2))])
    return operations

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
            s += "".join(map(str,l)) + "\n"
        return s

class LightGrid(Grid):
    def __init__(self, w):
        super().__init__(w, w, 0)

    def run(self, operations):
        for op in operations:
            self.apply(op)

    def apply(self, operation):
        op, p0, p1 = operation

        x0, y0 = p0
        x1, y1 = p1

        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if op == "turn on":
                    self.set(x, y, 1)
                elif op == "turn off":
                    self.set(x, y, 0)
                elif op == "toggle":
                    self.set(x, y, 1 - g.get(x, y))
                else:
                    raise ValueError(f"Invalid operation {operation}")


input = aoc.input_as_string(aoc.challenge_filename(6, 2015))
lines = aoc.as_lines(input)
operations = parse(lines)
g = LightGrid(1000)
g.run(operations)

nb_lit = 0
for l in g.lines:
    nb_lit += sum(l)
print(nb_lit)

# g = LightGrid(10)
# print(g)
# test_instr = ["toggle 0,0 through 2,2"]
# test_ops = parse(test_instr)
# g.run(test_ops)
# print()
# print(g)

#
#
# print(nb_lit)
