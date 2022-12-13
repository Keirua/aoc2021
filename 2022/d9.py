import re
from typing import List, Tuple


class Tail:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.history: List[Tuple[int, int]] = []

    def follow(self, pos: Tuple[int, int]):
        x, y = pos
        dist_x = x - self.x
        dist_y = y - self.y
        dx = 1 if dist_x > 0 else -1
        dy = 1 if dist_y > 0 else -1
        if abs(dist_x) == 2 and dist_y == 0:
            self.x += dx
        elif abs(dist_y) == 2 and dist_x == 0:
            self.y += dy
        elif (abs(dist_y) == 2 and abs(dist_x) in (1, 2)) or (abs(dist_x) == 2 and abs(dist_y) in (1, 2)):
            self.x += dx
            self.y += dy
        self.history.append((self.x, self.y))


def part(moves: List[Tuple[str, int]], tails: List[Tail]) -> int:
    head: List[Tuple[int, int]] = [(0, 0)]
    mapping = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    for dir, dist in moves:
        dx, dy = mapping[dir]
        for i in range(dist):
            xh, yh = head[-1]
            xh, yh = xh + dx, yh + dy
            head.append((xh, yh))
            prev = head[-1]
            for r in range(len(tails)):
                tails[r].follow(prev)
                prev = tails[r].history[-1]

    return len(set(tails[-1].history))


if __name__ == "__main__":
    input = open(f"d9.txt").read()
    # input = open(f"d9-sample.txt").read()
    moves = [(dir, int(dist)) for (dir, dist) in re.findall(r"([RDLU]) (\d+)", input)]

    print(part(moves, [Tail()]))
    print(part(moves, [Tail() for _ in range(9)]))
