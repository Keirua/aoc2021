import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open(f"d11.txt").read()
lines = input.split("\n")
from collections import deque
class Monkey:
    def __init__(self):
        self.items = deque()
        self.op =""
        self.test = None
        self.on_true = None
        self.on_false = None

    def __repr__(self):
        items = "".join(list(map(str, self.items)))
        return f"<Monkey items={items} op={self.op} test={self.test} true={self.on_true} false={self.on_false}>"

    def calc_update(self, v, op):
        # todo : nice hack to test with eval/exec
        if op == 'old * 7':
            return v*7

        if op == 'old * old':
            return v*v

        if op == 'old + 8':
            return v+8

        if op == 'old + 4':
            return v+4

        if op == 'old + 3':
            return v+3

        if op == 'old + 5':
            return v+5

        if op == 'old + 7':
            return v+7

        if op == 'old * 3':
            return v*7

monkeys = []

for i in range(0, len(lines), 7):
    m = Monkey()
    m.items.append([int(s) for s in re.findall("(\d+)", lines[i+1])])
    m.op = re.findall("new = (.*)", lines[i+2])[0]
    m.test = int(re.findall("(\d+)", lines[i+3])[0])
    m.on_true = int(re.findall("(\d+)", lines[i+4])[0])
    m.on_false = int(re.findall("(\d+)", lines[i+5])[0])
    monkeys.append((m))

pp.pprint(monkeys)
# for i,m in enumerate(monkeys):
#     for i in range(len(m.items)):
#         m.items.pop()
