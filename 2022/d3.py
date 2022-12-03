sample="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

# data = sample.split("\n")
data = [l.strip() for l in open("d3.txt").readlines()]
total = 0
for d in data:
    s = len(d)
    l, r = set(d[0:s//2]), set(d[s//2:])
    common = ord(list(l&r)[0])
    if ord('a') <= common <= ord('z'):
        total += common - ord('a') +1
    else:
        total += common - ord('A') +27

print(total)
# print(data)