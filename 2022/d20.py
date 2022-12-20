from collections import deque
from typing import *


def parse(text: str) -> List[int]:
    return [int(l) for l in text.strip().splitlines()]


def encrypt(numbers: List[int], key: int = 1, nb_iterations: int = 1) -> int:
    """
    Move every number n from the list n position from their current position
    The trick is to use a second deque to keep track of the positions
    """
    L = len(numbers)
    values = deque([n * key for n in numbers])
    positions = deque(range(0, L))

    for _ in range(nb_iterations):
        for i in range(L):
            position = positions.index(i)
            # Put the current value in front so that we can remove it
            values.rotate(-position)
            positions.rotate(-position)
            current_value = values.popleft()
            current_position = positions.popleft()
            # then shift both deques again for insertion of the current values in the correct location
            values.rotate(-current_value)
            values.appendleft(current_value)
            positions.rotate(-current_value)
            positions.appendleft(current_position)

    # all the values are relative to the offset of zero so we can leave the deque in any order
    zero_offset = values.index(0)
    return sum([values[(zero_offset + i) % L] for i in [1000, 2000, 3000]])


test_text = open(f"d20-sample.txt").read()
test_numbers = parse(test_text)
assert (encrypt(test_numbers) == 3)
assert (encrypt(test_numbers, 811589153, 10) == 1623178306)
numbers = parse(open(f"d20.txt").read())
print(encrypt(numbers))
print(encrypt(numbers, 811589153, 10))
