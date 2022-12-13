import functools


def cmp(la, lb):
    if isinstance(la, int) and isinstance(lb, int):
        if la < lb:
            return -1
        if la == lb:
            return 0
        if la > lb:
            return 1
    if isinstance(la, int) and not isinstance(lb, int):
        return cmp([la], lb)
    if isinstance(lb, int) and not isinstance(la, int):
        return cmp(la, [lb])
    if isinstance(la, list) and isinstance(lb, list):
        for i in range(0, min(len(la), len(lb))):
            c = cmp(la[i], lb[i])
            if c in [-1, 1]:
                return c
        if len(la) == len(lb):
            return 0
        if len(la) < len(lb):  # left list ran out of items first -> correct order
            return -1
        if len(la) > len(lb):  # right list ran out of items first -> incorrect order
            return 1
    raise "oops, should not happen"


assert (cmp([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == -1)
assert (cmp([7, 7, 7, 7], [7, 7, 7]) == 1)
assert (cmp([7, 7, 7], [7, 7, 7, 7]) == -1)
assert (cmp([], [3]) == -1)
assert (cmp([[1], [2, 3, 4]], [[1], 4]) == -1)
assert (cmp([9], [[8, 7, 6]]) != -1)
assert (cmp([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) == -1)
assert (cmp([[[]]], [[]]) != -1)
assert (cmp([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) != -1)

if __name__ == "__main__":
    p1 = 0
    packets = [
        [[2]],
        [[6]]
    ]
    input = open(f"d13.txt").read().strip()
    # input = open(f"d13-sample.txt").read().strip()
    lines = input.split("\n\n")
    for i, line in enumerate(lines):
        a, b = line.split("\n")

        a = eval(a.rstrip())
        b = eval(b.rstrip())
        packets.append(a)
        packets.append(b)
        if cmp(a, b) == -1:
            p1 += i+1

    print(p1)

    sorted_packets = sorted(packets, key=functools.cmp_to_key(cmp))
    p2 = (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1)
    print(p2)
