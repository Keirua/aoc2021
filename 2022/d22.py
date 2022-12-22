import re, pprint as pp
from dataclasses import dataclass


@dataclass
class Range:
    s: int
    e: int

    @classmethod
    def from_line(cls, line):
        e, s = 0, len(line)
        for i in range(len(line)):
            if line[i] != " ":
                s = i
                break
        for i in range(len(line) - 1, -1, -1):
            if line[i] != " ":
                e = i
                break
        return cls(s, e)

    @classmethod
    def from_col(cls, grid, x):
        e, s = 0, len(grid)
        for i in range(len(grid[0])):
            if grid[i][x] != " ":
                s = i
                break
        for i in range(len(grid[0]) - 1, -1, -1):
            if grid[i][x] != " ":
                e = i
                break
        return cls(s, e)



def parse(text):
    lines = text.splitlines()
    grid, instr = lines[:-2], lines[-1]
    moves = [m for m in re.findall(r"(\d+|L|R)", instr)]
    instructions = []
    for m in moves:
        try:
            intm = int(m)
            instructions.append(intm)
        except:
            assert(m in "RL")
            instructions.append(m)
    return Grid(grid), instructions


class Player:
    def __init__(self, x: int, y: int, o: str = "N"):
        assert (o in orientations)
        self.x = x
        self.y = y
        self.o = o

    def rotate(self, direction):
        i = orientations.index(self.o)
        if direction == "R":
            self.o = orientations[(i + 1) % len(orientations)]
        if direction == "L":
            self.o = orientations[(i + len(orientations) - 1) % len(orientations)]

    def password(self):
        return 1000 * self.y + 4*self.x + orientations.index(self.o)

    def __str__(self):
        return f"<Player x={self.x} y={self.y} o={self.o}>"


class Grid:
    def __init__(self, lines: [[str]]):
        self.lines = [list(l.rstrip("\n")) for l in lines]
        self.hranges = [Range.from_line(l) for l in lines]
        self.vranges = [Range.from_col(lines, j) for j in range(len(lines))]

    def next_cell(self, p: Player):
        dx, dy = dir_mapping[p.o]
        nx, ny = p.x + dx, p.y + dy
        print(dx, dy, nx, ny)
        # print(dx, dy, nx, ny)
        hr = self.hranges[p.y]
        vr = self.vranges[p.x]
        if not (hr.s <= nx <= hr.e and vr.s <= ny <= vr.e):
            if p.o == ">":
                nx = self.hranges[p.y].s
            if p.o == "<":
                nx = self.hranges[p.y].e
            if p.o == "^":
                ny = self.vranges[p.x].s
            if p.o == "v":
                ny = self.vranges[p.y].e
        return (nx, ny, self.lines[ny][nx])

    def run(self, instructions:[int|str], player):
        for instr in instructions:
            assert ((isinstance(instr, str) and instr in "LR") or isinstance(instr, int))
            if isinstance(instr, str) and instr in "LR":
                player.rotate(instr)
            else:
                i = 0
                assert (instr is not None), instr
                while i < instr:
                    self.lines[player.y][player.x] = player.o
                    nx, ny, c = self.next_cell(player)
                    print(player.x, player.y, player.o, dir_mapping[player.o], nx, ny, c)
                    if c != "#":
                        player.x, player.y = nx, ny
                        i += 1
                    else:
                        break
            self.lines[player.y][player.x] = player.o

    def __str__(self):
        return "\n".join(["".join(l) for l in self.lines])



orientations = [">", "v", "<", "^"]  # turn right = current orientation +1 % 4
dir_mapping = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
}

text = open(f"d22-sample.txt").read()
grid, instructions = parse(text)
player = Player(grid.hranges[0].s, 0, ">")

assert(Player(8, 6, ">").password() == 6032) # row 6, col 8, facing right -> 6032
# pp.pprint(instructions)
# print(grid.hranges[0])
# print(grid.vranges[0])
# print(grid.vranges[9])
# print(player)
# print(grid.next_cell(player))
# print(grid.next_cell(Player(12, 0, "W")))
grid.run(instructions, player)
print(player)
print(player.password())
print(grid)