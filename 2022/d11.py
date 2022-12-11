import re, pprint as pp
from math import prod
import copy
from typing import List, Callable, Optional
from collections import Counter
from dataclasses import dataclass
from functools import partial


@dataclass
class Monkey:
    items: Counter
    operation_code: str = ""
    op: Callable[[int], int] = None
    test: Optional[int] = None
    on_true: Optional[int] = None
    on_false: Optional[int] = None
    nb_inspect: int = 0

    @classmethod
    def from_lines(cls: "Monkey", lines: List[str]) -> "Monkey":
        operation_code = re.search(r"new = (.*)", lines[2]).group(1)
        return cls(
            items=Counter([int(s) for s in re.findall("(\d+)", lines[1])]),
            operation_code=operation_code,
            op=lambda old: eval(operation_code),
            test=int(lines[3].split()[-1]),
            on_true=int(lines[4].split()[-1]),
            on_false=int(lines[5].split()[-1])
        )

    def __repr__(self):
        items = ", ".join(list(map(str, self.items)))
        return f"<Monkey items={items} op={self.operation_code} test={self.test} true={self.on_true} false={self.on_false}>"


def parse(raw_monkeys: List[str]) -> List[Monkey]:
    return [Monkey.from_lines(m.split("\n")) for m in raw_monkeys]


def run(monkeys: List[Monkey], part: int, N: int) -> int:
    lcm = prod([m.test for m in monkeys])
    for nb_runs in range(N):
        for m in monkeys:
            for old, nb_old in m.items.items():
                if part == 2:
                    new = m.op(old) % lcm
                else:
                    new = m.op(old) // 3
                if new % m.test == 0:
                    monkeys[m.on_true].items[new] += nb_old
                else:
                    monkeys[m.on_false].items[new] += nb_old
                m.nb_inspect += nb_old
            m.items = Counter()

    inspects = sorted([m.nb_inspect for m in monkeys])
    return inspects[-1] * inspects[-2]


part1 = partial(run, part=1, N=20)
part2 = partial(run, part=2, N=10000)

test_input = open(f"d11-sample.txt").read()
test_monkeys = parse(test_input.split("\n\n"))
test_monkeys2 = copy.deepcopy(test_monkeys)
assert (run(test_monkeys, 1, 20) == 10605)
assert (part1(parse(test_input.split("\n\n"))) == 10605)
assert (run(test_monkeys2, 2, 10000) == 2713310158)

input = open(f"d11.txt").read()
lines = input.split("\n\n")
monkeys = parse(lines)
pp.pprint(monkeys)
monkeys2 = copy.deepcopy(monkeys)
print(run(monkeys, 1, 20))
print(run(monkeys2, 2, 10000))
