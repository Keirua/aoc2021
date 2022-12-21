import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

# lines = open(f"d3-sample.txt").read().splitlines()
lines = open(f"d3.txt").read().splitlines()
p1 = 0
p2 = 0
digits = []
def is_triangle(a, b, c):
    return (a+b > c) and (a+c) > b and (b+c) > a
for l in lines:
    a,b,c = [int(i) for i in re.findall(r"(\d+)", l)]
    p1 += is_triangle(a,b,c)
    digits.append([a,b,c])

for i in range(0, len(digits), 3):
    l1, l2, l3 = digits[i], digits[i+1], digits[i+2]
    for j in range(3):
        p2 += is_triangle(l1[j], l2[j], l3[j])
        # 3182 is too high
pp.pprint(p1)
pp.pprint(p2)
