from common24 import extract_parameters
import itertools as it

# https://gist.github.com/jkseppan/1e36172ad4f924a8f86a920e4b1dc1b1
def backward(xcheck, yadd, zdiv, z_final, w):
    """Returns the possible values of z before a single block
    if the final value of z is z_final and input is w
    """
    zs = []
    x = z_final - w - yadd
    if x % 26 == 0:
        zs.append(x // 26 * zdiv)
    if 0 <= w - xcheck < 26:
        z0 = z_final * zdiv
        zs.append(w - xcheck + z0)

    return zs


def solve(part, div_check_add):
    zs = {0}
    result = {}
    if part == 1:
        ws = list(range(1, 10))
    else:
        ws = list(range(9, 0, -1))
    for zdiv, xcheck, yadd in div_check_add[::-1]:
        newzs = set()
        for w, z in it.product(ws, zs):
            z0s = backward(xcheck, yadd, zdiv, z, w)
            for z0 in z0s:
                newzs.add(z0)
                result[z0] = (w,) + result.get(z, ())
        zs = newzs
    return ''.join(map(str, result[0]))

input = open("input/24_2021.txt").read()
div_check_add = extract_parameters(input)
print(solve(1, div_check_add))
print(solve(2, div_check_add))