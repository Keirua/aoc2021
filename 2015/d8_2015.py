import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(8, 2015))
lines = aoc.as_lines(input)

def count_chars(s):
    s = s[1:-1]
    i = 0
    nb_chars = 0
    while i < len(s):
        if s[i] != "\\":
            nb_chars += 1
            i+=1
            continue
        else:
            if s[i+1] == "\\" or s[i+1] == "\"":
                nb_chars += 1
                i+=2
                continue
            if s[i+1]=="x":
                nb_chars += 1
                i += 4
                continue
    return nb_chars

assert(count_chars("\"abc\"") == 3)
assert(count_chars("\"\x27\"") == 1)
assert(count_chars("\"\\\\\"") == 1)

def part1(lines):
    # for l in lines:
    #     print(len(l))
    #
    # print()
    # for l in lines:
    #     print(count_chars(l))
    return (sum([len(l)-count_chars(l) for l in lines]))

test_input = aoc.input_as_string("input/8_2015_test.txt")
test_lines = aoc.as_lines(test_input)
print(part1(test_lines))
print(part1(lines))
