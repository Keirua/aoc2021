import pprint
import re

lines = [l.strip() for l in open("d7-sample.txt").readlines()]
lines = [l.strip() for l in open("d7.txt").readlines()]
def create_node(parent=None):
    return {
        "dirs": {},
        "files": {},
        "parent": parent
    }

tree = create_node()
curr_node = tree
history = []
for i in range(len(lines)):
    l = lines[i]
    if l.startswith("$ cd "):
        curr_step = l[len("$ cd "):]
        if curr_step == "..":
            history.pop()
            assert(curr_node)
            curr_node = curr_node["parent"]
        else:
            history.append(curr_step)
            if curr_step not in curr_node["dirs"].keys():
                curr_node["dirs"][curr_step] = create_node(curr_node)
            curr_node = curr_node["dirs"][curr_step]
    if l.startswith("$ ls"):
        done = False
        while i < len(lines)-1:
            i += 1
            if lines[i].startswith("dir "):
                dirname = lines[i][len("dir "):]
                if dirname not in curr_node["dirs"].keys():
                    curr_node["dirs"][dirname] = create_node(curr_node)
            elif re.match(r"^[0-9]", lines[i]):
                size, name = lines[i].split(" ")
                size = int(size)
                curr_node["files"][name] = size
            else:
                break

SIZES = {}
def compute_sizes(tree):
    if id(tree) in SIZES:
        return SIZES[id(tree)]
    print(tree["files"].values())
    filesize = sum([f for f in tree["files"].values()])
    subdirsize = sum([compute_sizes(d) for d in tree["dirs"].values()])
    dirsize = filesize + subdirsize
    SIZES[id(tree)] = dirsize
    return dirsize


compute_sizes(tree)

part1 = sum([k for k in SIZES.values() if k < 100000])
print(SIZES)
print(part1)

import pprint as pp
stk = [tree]
smallest_size = 70000000000
smallest_dir = None
while len(stk) > 0:
    curr = stk.pop()
    for d in curr["dirs"].values():
        curr_d_size = compute_sizes(d)
        size_after_removal = compute_sizes(tree) - curr_d_size
        if size_after_removal < 40000000 and curr_d_size < smallest_size:
            smallest_size = curr_d_size
            smallest_dir = d
        stk.append(d)

print(smallest_size)

# pp.pprint(lines)
# print(history)
