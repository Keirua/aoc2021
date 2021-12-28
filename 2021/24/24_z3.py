from z3 import *
from common24 import extract_parameters

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
    assert(s.check() == sat)
    return s.model().eval(v)


input = open("input/24_2021.txt").read()
div_check_add = extract_parameters(input)
print(solve(div_check_add, True))
print(solve(div_check_add, False))
