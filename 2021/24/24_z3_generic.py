import z3
from common24 import parse_code
# https://www.reddit.com/r/adventofcode/comments/rnejv5/2021_day_24_solutions/hpshymr/
alu_program = parse_code(open('input/24_2021.txt', 'r').read())

solver = z3.Optimize()

zero, one = z3.BitVecVal(0, 64), z3.BitVecVal(1, 64)
digits = [z3.BitVec(f'd_{i}', 64) for i in range(14)]
for d in digits:
    solver.add(z3.And(1 <= d, d <= 9))
digit_input = iter(digits)

digits_base_10 = z3.BitVec(f"digits_base_10", 64)
solver.add(digits_base_10 == sum((10 ** i) * d for i, d in enumerate(digits[::-1])))

registers = {r: zero for r in 'xyzw'}

for i, instruction in enumerate(alu_program):
    # for every instruction, we create an intermediate value whose constraint is to
    # hold the result of this instruction
    if instruction[0] == 'inp':
        registers[instruction[1]] = next(digit_input)
    else:
        register, operand = instruction[1:]
        operand = registers[operand] if operand in registers else int(operand)
        instruction_i = z3.BitVec(f'instruction_{i}', 64)
        if instruction[0] == 'add':
            solver.add(instruction_i == registers[register] + operand)
        elif instruction[0] == 'mul':
            solver.add(instruction_i == registers[register] * operand)
        elif instruction[0] == 'mod':
            solver.add(registers[register] >= 0)
            solver.add(operand > 0)
            solver.add(instruction_i == registers[register] % operand)
        elif instruction[0] == 'div':
            solver.add(operand != 0)
            solver.add(instruction_i == registers[register] / operand)
        elif instruction[0] == 'eql':
            solver.add(instruction_i == z3.If(registers[register] == operand, one, zero))
        else:
            assert False
        registers[register] = instruction_i

solver.add(registers['z'] == 0)

for f in (solver.maximize, solver.minimize):
    solver.push()
    f(digits_base_10)
    assert(solver.check() == z3.sat)
    print(solver.model().eval(digits_base_10))
    solver.pop()