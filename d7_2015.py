import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)
import functools
from operator import rshift, lshift, __and__, __or__

class Cpu:
    def __init__(self):
        self.data = {}

    def run(self, lines):
        self.data = {}
        for line in lines:
            raw_operation, target = line.split(" -> ")
            self.data[target.strip()] = raw_operation

    @functools.lru_cache()
    def get_value(self, key):
        if re.match(r"^\d+$", key):
            return int(key)
        op = self.data[key].split(" ")

        if len(op) == 1:
            if re.match(r"^\d+$", op[0]):
                return int(op[0])
            else:
                return self.get_value(op[0])
        operators = {
            "AND": __and__,
            "OR": __or__,
            "LSHIFT": lshift,
            "RSHIFT": rshift
        }
        if op[1] in operators.keys():
            return operators[op[1]](self.get_value(op[0]), self.get_value(op[2]))
        if "NOT" in op:
            # tricky part I had to lookup: we want to stay on uint16
            return ~self.get_value(op[1])&0xFFFF
        # should not happen
        raise ValueError(self.data[key])

cpu = Cpu()
test_input = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""
test_lines = aoc.as_lines(test_input)

input = aoc.input_as_string(aoc.challenge_filename(7, 2015))
lines = aoc.as_lines(input)
cpu.run(test_lines)
print(cpu.get_value("i"))
cpu.run(lines)
print(cpu.get_value("a"))