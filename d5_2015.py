import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(5, 2015))
lines = aoc.as_lines(input)

def is_nice(s):
    for f in ["ab", "cd", "pq", "xy"]:
        if f in s:
            return False
    vowels = "aeiou"
    nb_vowels = 0
    has_double = False
    for i in range(len(s)):
        if s[i] in vowels:
            nb_vowels += 1
        if i>=1 and s[i-1] == s[i]:
            has_double = True
    return has_double and nb_vowels >= 3

assert(is_nice("ugknbfddgicrmopn"))
assert(is_nice("aaa"))
assert(not is_nice("jchzalrnumimnmhp"))
assert(not is_nice("haegwjzuvuyypxyu"))
assert(not is_nice("dvszwmarrgswjxmb"))

nb_nice1 = len(list(filter(is_nice, lines)))
pp.pprint(lines)
pp.pprint(len(lines))
pp.pprint(nb_nice1)
