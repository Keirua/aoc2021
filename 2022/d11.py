import re, pprint, itertools as it
from math import prod
import copy
pp = pprint.PrettyPrinter(indent=4)

from collections import Counter
class Monkey:
    def __init__(self):
        self.items = None
        self.op = ""
        self.test = None
        self.on_true = None
        self.on_false = None
        self.nb_inspect = 0

    @classmethod
    def from_lines(cls, lines):
        m = cls()
        items = []
        for s in re.findall("(\d+)", lines[1]):
            items.append(int(s))
        m.items = Counter(items)
        m.op = re.findall("new = (.*)", lines[2])[0]
        m.test = int(re.findall("(\d+)", lines[3])[0])
        m.on_true = int(re.findall("(\d+)", lines[4])[0])
        m.on_false = int(re.findall("(\d+)", lines[5])[0])
        return m

    def __repr__(self):
        items = ", ".join(list(map(str, self.items)))
        return f"<Monkey items={items} op={self.op} test={self.test} true={self.on_true} false={self.on_false}>"

def parse(lines):
    return [Monkey.from_lines(lines[i:i+7]) for i in range(0, len(lines), 7)]


def run(monkeys, part, N):
    lcm = prod([m.test for m in monkeys])
    for nb_runs in range(N):
        for m in monkeys:
            for old, nb_old in m.items.items():
                if part == 2:
                    v = eval(m.op) % lcm
                else:
                    v = eval(m.op) // 3
                if v % m.test == 0:
                    monkeys[m.on_true].items[v] += nb_old
                else:
                    monkeys[m.on_false].items[v] += nb_old
                m.nb_inspect += nb_old
            m.items = Counter()

    inspects = list(sorted([m.nb_inspect for m in monkeys]))
    return(inspects[-1]*inspects[-2])


test_input = open(f"d11-sample.txt").read()
test_monkeys = parse(test_input.split("\n"))
test_monkeys2 = copy.deepcopy(test_monkeys)
assert(run(test_monkeys, 1, 20) == 10605)
assert(run(test_monkeys2, 2, 10000) == 2713310158)

input = open(f"d11.txt").read()
lines = input.split("\n")
monkeys = parse(lines)
monkeys2 = copy.deepcopy(monkeys)
print(run(monkeys, 1, 20))
print(run(monkeys2, 2, 10000))
