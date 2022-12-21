import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)
from hashlib import md5
input = 'uqwqemis'

def encrypt(s):
    return md5(bytes(s, "utf-8")).hexdigest()
def part1(input):
    pw = ""
    i = 0
    # input = "abc"
    # i = 3231900
    while len(pw) < 8:
        s = input + str(i)
        hash = encrypt(s)
        # print(s, hash)
        if hash.startswith("00000"):
            pw += hash[5]
            print("password", pw)
        i += 1
    print("Final password", pw)
    return pw

def part2(input):
    pw = ["_" for i in range(8)]
    i = 0
    # input = "abc"
    # i = 3231900
    while any([p == "_" for p in pw]):
        s = input + str(i)
        hash = encrypt(s)
        # print(s, hash)
        if hash.startswith("00000"):
            pos = hash[5]
            if pos in "012345678" and pw[int(pos)] == "_":
                pw[int(pos)] = hash[6]
                print("password", "".join(pw))
        i += 1
    print("Final password", "".join(pw))
    return pw

part2(input)