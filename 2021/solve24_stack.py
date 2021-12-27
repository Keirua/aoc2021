import re


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
    return div_check_add


def solve(inp, occurences) -> str:
    """Solve the problem
    """
    zstack = []
    for i, oc in enumerate(occurences):
        div, chk, add = list(map(int, oc))
        if div == 1:
            zstack.append((i, add))
        elif div == 26:
            j, add = zstack.pop()
            inp[i] = inp[j] + add + chk
            if inp[i] > 9:
                inp[j] = inp[j] - (inp[i] - 9)
                inp[i] = 9
            if inp[i] < 1:
                inp[j] = inp[j] + (1 - inp[i])
                inp[i] = 1
        else:
            raise (ValueError(f"unsupported div value: {div}"))
    assert (len(zstack) == 0), len(zstack) # the stack must be 0 in order for z to reach 0 at the end
    return "".join(map(str, inp))


def part1(input):
    "biggest accepted number"
    inp = list([9] * 14)
    div_check_add = extract_parameters(input)
    return solve(inp, div_check_add)


def part2(input):
    """smallest accepted number"""
    inp = list([1] * 14)
    div_check_add = extract_parameters(input)
    return solve(inp, div_check_add)


input = open("input/24_2021.txt").read()
print(part1(input))
print(part2(input))
