import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = open("d4-sample.txt")
input = open("d4.txt")


def is_in(a, b, c, d): return c in range(a, b + 1) and d in range(a, b + 1)


p1 = 0
p2 = 0
# for line in input:
# l,r = line.split(",")
# a, b = l.split("-")
# c, d = r.split("-")
# a,b,c,d = int(a), int(b), int(c), int(d)
for line in input:
    a, b, c, d = [int(v) for v in re.findall(r'(\d+)', line)]
    p1 += is_in(a, b, c, d) or is_in(c, d, a, b)
    r1 = set(range(a, b + 1))
    r2 = set(range(c, d + 1))
    p2 += len(r1 & r2) > 0
pp.pprint(p1)
pp.pprint(p2)
