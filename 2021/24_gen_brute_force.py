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
    assert (len(zstack) == 0), len(zstack)  # the stack must be 0 in order for z to reach 0 at the end
    return "".join(map(str, inp))


def gen_tpl(w, zdivisor, xadder, yadder):
    return f"""    z = z/{zdivisor}
    if (z%26)+({xadder}) != input[{w}]:
	     z = 26*z + input[{w}] + ({yadder})
"""


def generate_bruteforce(input):
    occurences = extract_parameters(input)
    print("def check(input):")
    print("    z = 0")
    for i, oc in enumerate(occurences):
        div, chk, add = list(map(int, oc))
        print(gen_tpl(i, div, chk, add))
    print("    return z == 0")


input = open("input/24_2021.txt").read()
generate_bruteforce(input)
