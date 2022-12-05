import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open("d5.txt").read()
lines = input.split("\n")
stacks = [[] for i in range(9+1)]

N = 9
for s in range(N):
    for i in range(7, -1, -1):
        v = lines[i][4*s+1]
        if v != " ":
            stacks[s].append(v)
# print(stacks)
moves = []
for (nb, src, dst) in re.findall(r"move (\d+) from (\d+) to (\d+)", input):
    moves.append([int(nb), int(src)-1, int(dst)-1])
# print(moves)
# def part1(stacks, moves):
#     for (nb, src, dst) in moves:
#         for i in range(nb):
#             if len(stacks[src]) > 0:
#                 stacks[dst].append(stacks[src].pop())
#     print(stacks)
#     m = ""
#     for s in stacks:
#         if len(s):
#             m += s[-1]
#     print(m)

for (nb, src, dst) in moves:
    tmp = []
    for i in range(nb):
        if len(stacks[src]) > 0:
            tmp.append(stacks[src].pop())
    tmp = tmp[::-1]
    stacks[dst] = stacks[dst] + tmp
print(stacks)
m = ""
for s in stacks:
    if len(s):
        m += s[-1]
print(m)