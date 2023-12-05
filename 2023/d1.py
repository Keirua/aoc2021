import re
import string


def parse(line):
    digits = re.findall(r"\d", line)
    return int(digits[0] + digits[-1])

def parse2(line):
    values = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    matches = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line)
    v0 = values.get(matches[0], matches[0])
    rpos = {k: line.rfind(k) for k in list(values.keys()) + list(string.digits) if line.rfind(k) != -1}
    rightmost = max(rpos, key=rpos.get)
    v1 = values.get(rightmost, rightmost)

    return int(v0 + v1)


def part1(file):
    with open(file) as f:
        lines = f.readlines()
        return sum([parse(l.strip().lower()) for l in lines])

def part2(file):
    with open(file) as f:
        lines = f.readlines()
        return sum([parse2(l.strip().lower()) for l in lines])

print(part1("d1.txt"))
print(part2("d1.sample"))
print(part2("d1.sample2"))
print(part2("d1.sample2"))
print(part2("d1.txt"))
