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
            # print(i, X, i*X)
            tot += i * X
        X += adds[i]
    return tot


grid = [['.' for _ in range(40)] for _ in range(6)]
x = 1
t = 0
def cell_value(x, t1):
    if abs(x - (t1 % 40)) <= 1:
        return "#"
    return ' '

for line in lines:
    instruction = line.split()
    if instruction[0] == 'noop':
        grid[t // 40][t % 40] = cell_value(x, t)
        t += 1
    elif instruction[0] == 'addx':
        grid[t // 40][t % 40] = cell_value(x, t)
        t += 1
        grid[t // 40][t % 40] = cell_value(x, t)
        t += 1
        x += int(instruction[1])

print(part1(adds))
for y in range(6):
    print(''.join(grid[y]))