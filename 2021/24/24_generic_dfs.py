from common24 import parse_code

# https://github.com/WilliamLP/AdventOfCode/blob/master/2021/day24.py
# There is nothing particularly elegant about my solution but I'm posting it in case anyone is interested, and it gets there!
#
# I noticed the input code had 14 very similar chunks that each took a single input, and the only thing that mattered about the state between chunks was z and input w registers -- x and y are zeroed out each time. So I basically just did a DFS with depth 14 and memoization on the branches, trying to find z=0 at the final step. And I added a cache for the execution to speed up part 2. Part 2 took 8 minutes runtime.
REGS = {'w': 0, 'x': 1, 'y': 2, 'z': 3}


def execute(line, regs, input_arr):
    instruction, register, operand = line
    if instruction == 'inp':
        regs[REGS[register]] = int(input_arr.pop(0))
    else:
        if operand in REGS.keys():
            n = regs[REGS[operand]]
        else:
            n = int(operand)
        if instruction == 'add':
            regs[REGS[register]] += n
        elif instruction == 'mul':
            regs[REGS[register]] *= n
        elif instruction == 'mod':
            regs[REGS[register]] %= n
        elif instruction == 'div':
            regs[REGS[register]] //= n
        elif instruction == 'eql':
            regs[REGS[register]] = 1 if regs[REGS[register]] == n else 0


MEMO2 = {}


def execute_all(chunks, pos, input, z):
    key = f'{pos} {input} {z}'
    if key in MEMO2:
        return MEMO2[key]
    regs = [0, 0, 0, z]
    input_arr = list(str(input))
    for line in chunks[pos]:
        execute(line, regs, input_arr)
    res = regs[REGS['z']]
    MEMO2[key] = res
    return res


MEMO = {}
MIN_Z = 999999


def find(chunks, pos, z):
    global MIN_Z

    key = f'{pos} {z}'
    if key in MEMO:
        return MEMO[key]
    found = None

    # PART 1
    # for i in (9,8,7,6,5,4,3,2,1):
    # PART 2
    for i in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        exec_result = execute_all(chunks, pos, i, z)
        if (pos == 13):
            if abs(exec_result) < MIN_Z:
                print(f'Min z {exec_result}')
                MIN_Z = abs(exec_result)
            if exec_result == 0:
                found = [i]
                break
            else:
                found = None
        else:
            new_found = find(chunks, pos + 1, exec_result)
            if new_found:
                found = [i] + new_found
                break

    MEMO[key] = found
    return found


def extract_chunks_from_code(code):
    chunks = []
    rest = code
    while rest:
        chunks.append(rest[0:18])
        rest = rest[18:]
    return chunks


def main():
    code = parse_code(open('input/24_2021.txt').read())
    chunks = extract_chunks_from_code(code)

    res = find(chunks, 0, 0)
    print(f"Part 2 Answer: {''.join([str(ch) for ch in res])}")


main()
