import  pprint as pp, itertools as it

OP = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a/b,
}

lines = open(f"d21.txt").read().splitlines()
def parse(lines):
    values = {}
    operations = {}
    for l in lines:
        name, content = l.split(": ")
        try:
            values[name] = int(content)
        except:
            operations[name] = content.split(" ")
    return values, operations

def part1(lines):
    values, operations = parse(lines)

    def get(k):
        if k not in values.keys():
            v = OP[operations[k][1]](get(operations[k][0]), get(operations[k][2]))
            values[k] = v
        return values[k]

    # pp.pprint(values)
    # pp.pprint(operations)
    print(get("root"))


def part1_z3(lines):
    values, operations = parse(lines)
    # values["humn"] = None
    vars = {}
    s = Solver()
    for k in list(operations.keys()) + list(values.keys()):
        vars[k] = Int(k)
    for k in values.keys():
        s.add(vars[k] == values[k])
    for k in operations.keys():
        o = operations[k]
        s.add(vars[k] == OP[o[1]](vars[o[0]], vars[o[2]]))
    s.check()
    m = s.model()
    print(m[vars["root"]].as_long())

from z3 import *
def part2(lines):
    values, operations = parse(lines)
    # values["humn"] = None
    vars = {}
    s = Solver()
    for k in list(operations.keys()) + list(values.keys()):
        vars[k] = Int(k)
    for k in values.keys():
        s.add(vars[k] == values[k])
    for k in operations.keys():
        o = operations[k]
        s.add(vars[k] == OP[o[1]](vars[o[0]], vars[o[2]]))
    s.check()
    m = s.model()
    print(m[vars["root"]].as_long())

part1(lines)
part2(lines)

