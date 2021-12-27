import re
from z3 import *


def extract_parameters(program):
    repeated_program = r"""inp w
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

    div_check_add = re.findall(repeated_program, program)
    assert (len(div_check_add) == 14), len(div_check_add)
    return [list(map(int, dca)) for dca in div_check_add]

def solve(div_check_add: list, should_maximize:bool=True) -> int:
    s = Optimize()
    z = 0  # this is our running z, which has to be zero at the start and end
    v = 0  # this is the value from concatenating our digits
    ws = [Int(f'w{i}') for i in range(14)]
    for (i,[div,check,add]) in enumerate(div_check_add):
        v = v * 10 + ws[i]
        s.add(And(ws[i] >= 1, ws[i] <= 9))
        z = If(z % 26 + check == ws[i], z / div, z / div * 26 + ws[i] + add)
    s.add(z == 0)
    if should_maximize:
        s.maximize(v)
    else:
        s.minimize(v)
    print(s.simplify(z))
    assert(s.check() == sat)
    return s.model().eval(v)


input = open("input/24_2021.txt").read()
div_check_add = extract_parameters(input)
print(solve(div_check_add, True))
print(solve(div_check_add, False))
