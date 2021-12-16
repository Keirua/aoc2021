import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(16, 2021))

mapping = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}
def parse(input):
    out = ""
    for c in input:
        out += mapping[c]
    return out

def to_int(b):
    """
    Converts a binary string (base 2, like 010011) to a base 10 integer (19)
    same as int(i, 2)
    """
    nb = 0
    l = len(b)
    p = 1
    for i in range(l):
        nb += p * int(b[l-i-1])
        p*=2
    return nb

from dataclasses import dataclass
@dataclass
class Packet:
    version: int
    type: int
    data: str


def extract(bits):
    # 110100101111111000101000
    # VVVTTTAAAAABBBBBCCCCC
    # bits = "110100101111111000101000"
    v = to_int(bits[0:3])
    t = to_int(bits[3:6])
    if type == 4:
        data = ""
        i = 0
        # parse type4: literal data
        # read by chunk of 5 bits, stop when the first bit of the last chunk is 0
        done = False
        while not done:
            # the first bit indicates when to stop
            if bits[6+5*i] == '0':
                done = True
            # the actual information is stored in the remaining 4 bits
            data += bits[6+5*i+1:6+5*i+5]
            i += 1

        # print(bits)
        return Packet(to_int(v), to_int(t), data)
    raise ValueError(t)


# pp.pprint(input)
bits = parse(input)
pp.pprint(extract(bits))