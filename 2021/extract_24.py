import re

program = r"""inp w
mul x 0
add x z
mod x 26
div z (.*)
add x (.*)
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (.*)
mul y x
add z y"""

day24 = open("input/24_2021.txt").read()
occurences = re.findall(program, day24)
assert(len(occurences) == 14)
for oc in occurences:
    print(list(map(int, oc)))