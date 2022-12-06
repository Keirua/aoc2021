import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open("d6.txt").read()
# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
N = 14
def part(t, N):
    for i in range(N,len(input)):
        values = set(input[i-N:i])
        # print(values)
        if len(values) == N:
            return i
print(part(input, 4))
print(part(input, 14))
