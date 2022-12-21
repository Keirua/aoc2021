import  pprint as pp, itertools as it

OP = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a//b,
}

lines = open(f"d21.txt").read().splitlines()
# lines = open(f"d21-sample.txt").read().splitlines()
values = {}
operations = {}
for l in lines:
    name, content = l.split(": ")
    try:
        values[name] = int(content)
    except:
        operations[name] = content.split(" ")

def get(k):
    if k not in values.keys():
        v = OP[operations[k][1]](get(operations[k][0]), get(operations[k][2]))
        values[k] = v
    return values[k]
pp.pprint(values)
pp.pprint(operations)
print(get("root"))