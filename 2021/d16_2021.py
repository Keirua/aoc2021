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
    length: int
    sub_packets: list


def extract(bits):
    # 110100101111111000101000
    # VVVTTTAAAAABBBBBCCCCC
    # bits = "110100101111111000101000"
    v = to_int(bits[0:3])
    t = to_int(bits[3:6])
    if t == 4:
        data = ""
        i = 0
        # parse type4: literal data
        # read by chunk of 5 bits, stop when the first bit of the last chunk is 0
        done = False
        while not done:
            # the actual information is stored in the remaining 4 bits
            data += bits[6+5*i+1:6+5*i+5]
            # the first bit indicates when to stop
            if bits[6+5*i] == '0':
                break
            i += 1
        return Packet(v, t, to_int(data), None, []), 6+5*i+5
    else:
        # everything that is not 4 is an operator packet
        # An operator packet contains one or more packets
        length_type_id = int(bits[6])
        if length_type_id == 0:
            # If the length type ID is 0, then the next 15 bits are a number
            # that represents the total length in bits of the sub-packets contained by this packet.
            length = to_int(bits[7:7+15])
            raise ValueError("not implemented")
        else:
            # If the length type ID is 1, then the next 11 bits are a number
            # that represents the number of sub-packets immediately contained by this packet.
            number_of_sub_packets = to_int(bits[7:7 + 11])
            packets = []
            total_offset = 0
            for i in range(number_of_sub_packets):
                new_packet, offset = extract(bits[18+total_offset:])
                # print(new_packet, offset)
                total_offset += offset
                packets.append(new_packet)
            return Packet(v,t, None, total_offset, packets), total_offset


    # raise ValueError(t)

# type 4 operator:
# So, this packet represents a literal value with binary representation
# 011111100101, which is 2021 in decimal.
# 110100101111111000101000
# VVVTTTAAAAABBBBBCCCCC

# length type 0:
# 00111000000000000110111101000101001010010001001000000000
# VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB

# length type 1
# 11101110000000001101010000001100100000100011000001100000
# VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC

# pp.pprint(input)
# bits = parse(input)
# pp.pprint(extract(bits))
assert(extract("110100101111111000101000") == (Packet(version=6, type=4, data=2021, length=None, sub_packets=[]), 21))
assert(extract("11101110000000001101010000001100100000100011000001100000") == (Packet(version=7, type=3, data=None, length=33, sub_packets=[Packet(version=2, type=4, data=1, length=None, sub_packets=[]), Packet(version=4, type=4, data=2, length=None, sub_packets=[]), Packet(version=1, type=4, data=3, length=None, sub_packets=[])]),33))