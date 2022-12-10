import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open(f"d10.txt").read().strip()
# input = open(f"d10-sample.txt").read().strip()
lines = input.split("\n")
adds = [0]
for l in lines:
    if l == "noop":
        adds.append(0)
    else:
        value = int(l.split(" ")[1])
        adds += [0, value]

def part1(adds):
    watch = [20,60,100,140,180, 220]
    X = 1
    tot = 0
    for i in range(220+1):
        if i in watch:
            print(i, X, i*X)
            tot += i * X
        X += adds[i]
    return tot

print(part1(adds))

# pp.pprint(lines)
