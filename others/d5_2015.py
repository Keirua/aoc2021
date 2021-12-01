import aoc

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

def has_repeated_pair(s):
    for i in range(0, len(s)-2):
        pair = s[i:i+2]
        for j in range(i+2, len(s)):
            pair2 = s[j:j+2]
            if pair == pair2:
                return True
    return False

def is_nice2(s):
    has_double_with_letter_between = False
    for i in range(2, len(s)):
        if s[i-2] == s[i]:
            has_double_with_letter_between = True
    return has_double_with_letter_between and has_repeated_pair(s)

assert(is_nice("ugknbfddgicrmopn"))
assert(is_nice("aaa"))
assert(not is_nice("jchzalrnumimnmhp"))
assert(not is_nice("haegwjzuvuyypxyu"))
assert(not is_nice("dvszwmarrgswjxmb"))
assert(is_nice2("qjhvhtzxzqqjkmpb"))
assert(is_nice2("xxyxx"))
assert(is_nice2("abcdefeghiab"))
assert(not is_nice2("aaa"))
assert(not is_nice2("uurcxstgmygtbstg"))
assert(not is_nice2("ieodomkazucvgmuy"))

nb_nice1 = len(list(filter(is_nice, lines)))
nb_nice2 = len(list(filter(is_nice2, lines)))

pp.pprint(nb_nice1)
pp.pprint(nb_nice2)
