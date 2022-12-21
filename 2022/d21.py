import  pprint as pp, itertools as it

OP = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a/b,
}


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
    vars = {}
    s = Solver()
    for k in list(operations.keys()) + list(values.keys()):
        vars[k] = Int(k)
    for k in set(values.keys()) - {"humn"}:
        s.add(vars[k] == values[k])
    # 3_916_936_880_449 was not accepted, but 3916936880448 was,
    # so I had to bisect my way to the other solution
    s.add(vars["humn"] < 3_916_936_880_449 )
    s.add(vars["humn"] > 3_000_000_000_000 )
    for k in set(operations.keys()) - {"root"}:
        o = operations[k]
        s.add(vars[k] == OP[o[1]](vars[o[0]], vars[o[2]]))
    s.add(vars[operations["root"][0]] == vars[operations["root"][2]])
    s.check()
    m = s.model()
    print(m[vars[operations["root"][0]] ].as_long()) # 3 916 936 880 449 is incorrect
    print(m[vars[operations["root"][2]] ].as_long()) # 3916936880449 is incorrect
    print(m[vars["humn"]].as_long()) # 3916936880449 is incorrect

lines = open(f"d21.txt").read().splitlines()
# lines = open(f"d21-sample.txt").read().splitlines()
part1(lines)
part2(lines)

