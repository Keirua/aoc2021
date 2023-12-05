import re
import string


def parse(line):
    digits = []
    for c in line:
        if c in string.digits:
            digits.append(c)
    return int(digits[0] + digits[-1])

def part1(file):
    p1 = 0
    with open(file) as f:
        lines = f.readlines()
        for l in lines:
            p1 += parse(l)
    return p1

print(part1("d1.sample"))
print(part1("d1.txt"))
