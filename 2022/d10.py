import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open(f"d10.txt").read().strip()
input = open(f"d10-sample.txt").read().strip()
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

def part2(adds):
    lines = [["." for i in range(40)] for i in range(6)]
    X = 0
    CRT_offset = 0
    print(len(adds))
    for i in range(len(adds)):
        if X-1 <= CRT_offset <= X+1:
            x = CRT_offset%40
            y = (CRT_offset-x)//40
            lines[y][x] = "#"
        X += adds[i]

        CRT_offset += 1
    for l in lines:
        print("".join(l))

# print(len(lines))
print(part1(adds))
part2(adds)
# pp.pprint(lines)
