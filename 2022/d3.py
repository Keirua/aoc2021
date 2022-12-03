sample="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def score(common):
    if ord('a') <= common <= ord('z'):
        return common - ord('a') + 1
    else:
        return common - ord('A') + 27

def part1(data):
    total = 0
    for d in data:
        s = len(d)
        l, r = set(d[0:s//2]), set(d[s//2:])
        common = ord(list(l&r)[0])
        total += score(common)
    return total

def part2(data):
    total = 0
    for l in range(0, len(data), 3):
        a, b, c = set(data[l]), set(data[l+1]), set(data[l+2])
        common = ord(list(a&b&c)[0])
        s = score(common)
        total += s
    return total

data = [l.strip() for l in open("d3.txt").readlines()]
# data = sample.split("\n")
p1 = part1(data)
p2 = part2(data)
print(p1, p2)
