import re, pprint
pp = pprint.PrettyPrinter(indent=4)

def parse(text):
    coords = []
    for line in text.split("\n"):
        coords.append(list(int(c) for c in re.findall(r"(-?\d+)", line)))
    return coords

text = open(f"d18.txt").read().rstrip()
coords = parse(text)
pp.pprint(coords)
