import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)
from hashlib import md5
input = 'uqwqemis'

def encrypt(s):
    return md5(bytes(s, "utf-8")).hexdigest()
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
