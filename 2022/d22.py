import re, pprint as pp

from enum import Enum
from dataclasses import dataclass


class InstructionType(Enum):
    Forward = 0
    Left = 1
    Right = 2


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
        for i in range(len(line)-1, -1, -1):
            if line[i] != " ":
                e = i
                break
        # print(s, e)
        return cls(s, e)



class Instruction:
    def __init__(self, type, amount=None):
        self.type = type
        self.amount = amount

    def __repr__(self):
        if self.type == InstructionType.Forward:
            return f"Forward {self.amount}"
        mapping = {InstructionType.Left: "L", InstructionType.Right: "R"}
        return f"Turn {mapping[self.type]}"


def parse(text):
    lines = text.splitlines()
    grid, instr = lines[:-2], lines[-1]
    moves = [m for m in re.findall(r"(\d+|L|R)", instr)]
    instructions = []
    for m in moves:
        try:
            intm = int(m)
            instructions.append(Instruction(InstructionType.Forward, intm))
        except:
            mapping = {"L": InstructionType.Left, "R": InstructionType.Right}
            instructions.append(Instruction(mapping[m]))
    return Grid(grid), instructions

class Player:
    def __init__(self, x, y, o="N"):
        self.x = x
        self.y = y
        self.o = o

    def rotate(self, direction):
        i = orientations.index(self.o)
        if direction == "R":
            self.o = orientations[(i + 1) % len(orientations)]
        if direction == "L":
            self.o = orientations[(i + len(orientations) - 1) % len(orientations)]

    def __str__(self):
        return f"<Player x={self.x} y={self.y} o={self.o}>"


class Grid:
    def __init__(self, lines: [[str]]):
        self.lines = lines
        self.hranges = [Range.from_line(l) for l in lines]
        self.vranges = []



orientations = ["N", "W", "S", "E"]  # turn right = current orientation +1 % 4
dir_mapping = {
    "N": (0, 1),
    "S": (0, -1),
    "W": (1, 0),
    "E": (-1, 0),
}

text = open(f"d22-sample.txt").read()
grid, instructions = parse(text)
player = Player(grid.hranges[0].s, 0, "R")
pp.pprint(instructions)
print(grid.hranges[0])
print(player)

