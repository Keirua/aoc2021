import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open(f"d11.txt").read()
input = open(f"d11-sample.txt").read()
lines = input.split("\n")
from collections import deque
class Monkey:
    def __init__(self):
        self.items = deque()
        self.op =""
        self.test = None
        self.on_true = None
        self.on_false = None
        self.nb_inspect = 0

    def __repr__(self):
        items = ", ".join(list(map(str, self.items)))
        return f"<Monkey items={items} op={self.op} test={self.test} true={self.on_true} false={self.on_false}>"


monkeys = []
for i in range(0, len(lines), 7):
    m = Monkey()
    for s in re.findall("(\d+)", lines[i + 1]):
        m.items.append(int(s))
    m.op = re.findall("new = (.*)", lines[i+2])[0]
    m.test = int(re.findall("(\d+)", lines[i+3])[0])
    m.on_true = int(re.findall("(\d+)", lines[i+4])[0])
    m.on_false = int(re.findall("(\d+)", lines[i+5])[0])
    monkeys.append((m))


def compute_runs(monkeys, N = 20):
    for nb_runs in range(N):
        for m in monkeys:
            nb_items = len(m.items)
            new_items = []
            for old in m.items:
                new_items.append(eval(m.op))
            to_true = [v for v in new_items if v % m.test == 0]
            to_false = [v for v in new_items if v % m.test != 0]
            monkeys[m.on_true].items += to_true
            monkeys[m.on_false].items += to_false
            m.items = deque()
            m.nb_inspect += nb_items
    inspects = list(sorted([m.nb_inspect for m in monkeys]))
    pp.pprint(inspects)
    return(inspects[-1]*inspects[-2])

print(compute_runs(monkeys, 1000))
