from hashlib import md5
import aoc

def hash(s):
    return md5(s.encode("utf-8")).hexdigest()

def search_hash(s, nb_zeros=5):
    i = 0
    target = "0" * nb_zeros
    while hash(s + str(i))[0:nb_zeros] != target:
        i = i+1
    return i

assert(search_hash("abcdef") == 609043)
assert(search_hash("pqrstuv") == 1048970)
input = aoc.input_as_string("../input/4_2015.txt")
print(search_hash(input))
print(search_hash(input, 6))
