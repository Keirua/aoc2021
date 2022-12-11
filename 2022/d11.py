import re, pprint as pp
from math import prod
import copy
from typing import List
from collections import Counter
class Monkey:
    def __init__(self):
        self.items = None
        self.operation_code = ""
        self.op = None
        self.test = None
        self.on_true = None
        self.on_false = None
        self.nb_inspect = 0

    @classmethod
    def from_lines(cls, lines):
        m = cls()
        m.items = Counter([int(s) for s in re.findall("(\d+)", lines[1])])
        m.operation_code = re.search(r"new = (.*)", lines[2]).group(1)
        m.op = lambda old: eval(m.operation_code)
        m.test = int(lines[3].split()[-1])
        m.on_true = int(lines[4].split()[-1])
        m.on_false = int(lines[5].split()[-1])
        return m

    def __repr__(self):
        items = ", ".join(list(map(str, self.items)))
        return f"<Monkey items={items} op={self.operation_code} test={self.test} true={self.on_true} false={self.on_false}>"

def parse(raw_monkeys:List[str]) -> List[Monkey]:
    return [Monkey.from_lines(m.split("\n")) for m in raw_monkeys]


def run(monkeys: List[Monkey], part: int, N: int) -> int:
    lcm = prod([m.test for m in monkeys])
    for nb_runs in range(N):
        for m in monkeys:
            for old, nb_old in m.items.items():
                if part == 2:
                    v = m.op(old) % lcm
                else:
                    v = m.op(old) // 3
                if v % m.test == 0:
                    monkeys[m.on_true].items[v] += nb_old
                else:
                    monkeys[m.on_false].items[v] += nb_old
                m.nb_inspect += nb_old
            m.items = Counter()

    inspects = sorted([m.nb_inspect for m in monkeys])
    return inspects[-1]*inspects[-2]


test_input = open(f"d11-sample.txt").read()
test_monkeys = parse(test_input.split("\n\n"))
test_monkeys2 = copy.deepcopy(test_monkeys)
assert(run(test_monkeys, 1, 20) == 10605)
assert(run(test_monkeys2, 2, 10000) == 2713310158)

input = open(f"d11.txt").read()
lines = input.split("\n\n")
monkeys = parse(lines)
pp.pprint(monkeys)
monkeys2 = copy.deepcopy(monkeys)
print(run(monkeys, 1, 20))
print(run(monkeys2, 2, 10000))
