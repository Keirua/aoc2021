import pprint as pp

lines = open(f"d7.txt").read().splitlines()
def parse(l):
    outsides = []
    insides = []
    curr = l
    while "[" in curr:
        open_br = curr.index("[")
        A, rest = curr[:open_br], curr[open_br + 1:]
        close_br = rest.index("]")
        inside, curr = rest[:close_br], rest[close_br + 1:]
        outsides.append(A)
        insides.append(inside)

    outsides.append(curr)
    return outsides, insides

def has_abba(w):
    return len(w) == 4 and w[0] != w[1] and w[0] == w[3] and w[1] == w[2]

p1 = 0
for line in lines:
    outsides, insides = parse(line)
    p1 += any(has_abba(w) for w in outsides) and not any(has_abba(w) for w in insides)
    # print(line, outsides, insides)
print(p1)
