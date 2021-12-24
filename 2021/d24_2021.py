import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)


def is_int(s):
    return not is_var(s)

valid_vars = "wxyz"

def is_var(s):
    return s in "wxyz"


class Alu:
    def __init__(self, instructions):
        self.instructions = instructions

    def run_with(self, input_data):
        self.vars = { k: 0 for k in valid_vars}
        self.input_data = input_data
        self.input_pos = 0
        return self.run_program()

    def run_program(self):
        # Then, after MONAD has finished running all of its instructions, it will indicate that the model number was
        # valid by leaving a 0 in variable z. However, if the model number was invalid, it will leave some other
        # non-zero value in z.
        for i in self.instructions:
            try:
                self.run_instruction(i)
            except ValueError:
                print("valueError Reached")
                return False
        return self.vars["z"] == 1

    def get_val(self, name):
        if is_var(name):
            return self.vars[name]
        return int(name)

    def run_instruction(self, instr):
        # inp a - Read an input value and write it to variable a.
        if instr[0] == "inp":
            assert(instr[1] in valid_vars)
            self.vars[instr[1]] = int(self.input_data[self.input_pos])
            self.input_pos += 1
            return
        a = self.vars[instr[1]]
        b = self.get_val(instr[2])
        # add a b - Add the value of a to the value of b, then store the result in variable a.
        if instr[0] == "add":
            self.vars[instr[1]] = a + b
        # mul a b - Multiply the value of a by the value of b, then store the result in variable a.
        if instr[0] == "mul":
            self.vars[instr[1]] = a * b
        # (Program authors should be especially cautious; attempting to execute div with b=0 or attempting to execute
        # mod with a<0 or b<=0 will cause the program to crash and might even damage the ALU. These operations are
        # never intended in any serious ALU program.).
        # div a b - Divide the value of a by the value of b, truncate the
        # result to an integer, then store the result in variable a. (Here, "truncate" means to round the value
        # toward zero.)
        if instr[0] == "div":
            if b == 0:
                raise ValueError("b = 0")
            else:
                self.vars[instr[1]] = a // b
        # mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also
        # called the modulo operation.)
        if instr[0] == "mod":
            b = self.get_val(instr[2])
            if a < 0 or b <= 0:
                raise ValueError("a < 0 or b <= 0")
            else:
                self.vars[instr[1]] = a % b
        # eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the
        # value 0 in variable a.
        if instr[0] == "eql":
            self.vars[instr[1]] = int(a==b)

def parse(input):
    instructions = [l.rstrip().split(" ") for l in aoc.as_lines(input)]
    return instructions


input = aoc.input_as_string(aoc.challenge_filename(24, 2021))
instructions = parse(input)

sample = "13579246899999"
a = Alu(instructions)

for i in range(99999999999999, 0, -1):
    v = str(i)
    if "0" in v:
        continue
    if (a.run_with(v)):
        print(v)