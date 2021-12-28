import z3

# https://www.reddit.com/r/adventofcode/comments/rnejv5/2021_day_24_solutions/hpshymr/

prog = [line.split() for line in open('input/24_2021.txt', 'r').read().splitlines()]

solver = z3.Optimize()

zero, one = z3.BitVecVal(0, 64), z3.BitVecVal(1, 64)
digits = [z3.BitVec(f'd_{i}', 64) for i in range(14)]
for d in digits:
    solver.add(And(1 <= d, d <= 9))
digit_input = iter(digits)

registers = {r: zero for r in 'xyzw'}

for i, inst in enumerate(prog):
    if inst[0] == 'inp':
        registers[inst[1]] = next(digit_input)
        continue
    a, b = inst[1:]
    b = registers[b] if b in registers else int(b)
    c = z3.BitVec(f'v_{i}', 64)
    if inst[0] == 'add':
        solver.add(c == registers[a] + b)
    elif inst[0] == 'mul':
        solver.add(c == registers[a] * b)
    elif inst[0] == 'mod':
        solver.add(registers[a] >= 0)
        solver.add(b > 0)
        solver.add(c == registers[a] % b)
    elif inst[0] == 'div':
        solver.add(b != 0)
        solver.add(c == registers[a] / b)
    elif inst[0] == 'eql':
        solver.add(c == z3.If(registers[a] == b, one, zero))
    else:
        assert False
    registers[a] = c

solver.add(registers['z'] == 0)

for f in (solver.maximize, solver.minimize):
    solver.push()
    f(sum((10 ** i) * d for i, d in enumerate(digits[::-1])))
    print(solver.check())
    m = solver.model()
    print(''.join(str(m[d]) for d in digits))
    solver.pop()