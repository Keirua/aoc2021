import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open(f"d11.txt").read()
input = open(f"d11-sample.txt").read()
lines = input.split("\n")
from collections import deque, Counter
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
    items = []
    for s in re.findall("(\d+)", lines[i + 1]):
        items.append(int(s))
    m.items = Counter(items)
    m.op = re.findall("new = (.*)", lines[i+2])[0]
    m.test = int(re.findall("(\d+)", lines[i+3])[0])
    m.on_true = int(re.findall("(\d+)", lines[i+4])[0])
    m.on_false = int(re.findall("(\d+)", lines[i+5])[0])
    monkeys.append((m))

# for j in range(20):
#     for i,m in enumerate(monkeys):
#         for i in range(len(m.items)):
#             old = m.items.popleft()
#             n = eval(m.op) // 3
#             m.nb_inspect+=1
#             if n % m.test == 0:
#                 monkeys[m.on_true].items.append(n)
#             else:
#                 monkeys[m.on_false].items.append(n)

for nb_runs in range(1000):
    if nb_runs % 100 == 0:
        print(nb_runs)
    for m in monkeys:
        for old, nb_old in m.items.items():
            v = eval(m.op) // 3
            if v % m.test == 0:
                monkeys[m.on_true].items[v] += nb_old
            else:
                monkeys[m.on_false].items[v] += nb_old
            m.nb_inspect += nb_old
        m.items = Counter()

inspects = list(sorted([m.nb_inspect for m in monkeys]))
pp.pprint(inspects)
print(inspects[-1]*inspects[-2])

