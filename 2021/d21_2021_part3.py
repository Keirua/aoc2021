import pprint
from functools import lru_cache
import itertools as it

pp = pprint.PrettyPrinter(indent=4)

@lru_cache(maxsize=None)
def next_position(current_position: int, three_dices: int) -> int:
    """The new position on the board, once you move"""
    return (current_position + three_dices - 1) % 10 + 1

@lru_cache()
def all_dices():
    dices = [a+b+c  for a,b, c in it.product(range(1, 4), range(1, 4), range(1, 4))]
    return dices


@lru_cache(maxsize=None)
def part3(p0, p1, s0=0, s1=0, current=0):
    """
    p0, p1 are the positions of the players 0 and 1
    s0, s1 are the scores of the players 0 and 1
    current is the index of the current player
    """
    if s0 >= 100:
        return [1, 0]  # 1 more win for player 0
    if s1 >= 100:
        return [0, 1]
    ans = [0, 0]

    # Generate all the new dices
    for dice3 in all_dices():
        # then we update the positions and scores depending on who’s turn it is to play
        if current == 0:
            new_p0 = next_position(p0, dice3)
            new_s0 = s0 + new_p0
            # we search for the winner in this sub-universe
            # (thanks lru_cache: there are not that many possibilities, so a lot of duplicates)
            partial = part3(new_p0, p1, new_s0, s1, 1)
        else:
            new_p1 = next_position(p1, dice3)
            new_s1 = s1 + new_p1
            partial = part3(p0, new_p1, s0, new_s1, 0)
        # and we update the global winner scoreboard
        ans = [ans[0] + partial[0], ans[1] + partial[1]]
    return ans


print(max(part3(4, 8)))
