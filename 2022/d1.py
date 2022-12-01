sample = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

data = [l.rstrip("\n") for l in open("d1.txt").readlines()]
snacks = []
curr = 0
for d in data:
    if d == "":
        snacks.append(curr)
        curr = 0
    else:
        curr += int(d)
snacks = list(sorted(snacks))
print(snacks[-1])
print(sum(snacks[-3:]))