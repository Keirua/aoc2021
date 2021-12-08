import aoc

def parse(input:str):
    lines = aoc.as_lines(input)
    return aoc.as_ints(lines)

def part_1(ints) -> int:
    nb_inc = 0
    for i in range(len(ints)-1):
        if ints[i+1] > ints[i]:
            nb_inc += 1
    return nb_inc

def part_2(ints) -> int:
    nb_inc = 0
    for i in range(len(ints)-3):
        # it is worth noting that we can avoid the sum and compare 2 ints:
        # s < s2
        # <=> ints[i]+ints[i+1]+ints[i+2] < ints[i+1]+ints[i+2]+ints[i+3]
        # <=> ints[i] < ints[i+3]
        s = sum(ints[i:i+3])
        s2 = sum(ints[i+1:i+4])
        if s2 > s:
            nb_inc += 1
    return nb_inc

if __name__ == "__main__":
    input = aoc.input_as_string(aoc.challenge_filename(1, 2021))
    ints = parse(input)
    print(part_1((ints)))
    print(part_2((ints)))