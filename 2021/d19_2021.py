import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(19, 2021))
test_input1 = aoc.input_as_string("input/2021_19.test.txt")
test_input0 = """--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1"""



def parse(input):
    lines = aoc.as_lines(input)
    i = 0
    scanners = []
    while i < len(lines):
        if "scanner" in lines[i]:
            i+= 1
            scanner= []
            while i < len(lines) and lines[i] != "":
                pos = list(map(int, lines[i].split(",")))
                scanner.append(pos)
                i+= 1
            scanners.append(scanner)

        i += 1
    return scanners

# pp.pprint(lines)
pp.pprint(parse(test_input0))
pp.pprint(parse(test_input1))