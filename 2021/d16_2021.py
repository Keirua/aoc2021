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

sum_version = 0

def extract(bits, depth=0):
    global sum_version
    tabs = "\t"*depth
    v = to_int(bits[0:3])
    t = to_int(bits[3:6])
    print(f"{tabs}v: {v}")
    print(f"{tabs}t: {t}")
    if t == 4:
        print(f"{tabs}literal value packet")
        data = ""
        i = 0
        # parse type4: literal data
        # read by chunk of 5 bits, stop when the first bit of the last chunk is 0
        while True:
            # the actual information is stored in the remaining 4 bits
            data += bits[6+5*i+1:6+5*i+5]
            # the first bit indicates when to stop
            if bits[6+5*i] == '0':
                break
            i += 1

        sum_version += v
        return Packet(v, t, to_int(data), None, []), 6+5*i+5
    else:
        print(f"{tabs}operator packet")
        # everything that is not 4 is an operator packet
        # An operator packet contains one or more packets
        length_type_id = int(bits[6])
        print(f"{tabs}length_type_id: {length_type_id}")
        if length_type_id == 0:
            # If the length type ID is 0, then the next 15 bits are a number
            # that represents the total length in bits of the sub-packets contained by this packet.
            length = to_int(bits[7:7+15])
            print(f"{tabs}length: {length}")
            total_offset = 0
            packets = []
            while total_offset < length:
                new_packet, offset = extract(bits[22 + total_offset:], depth+1)
                total_offset += offset
                packets.append(new_packet)
            sum_version += v
            return Packet(v, t, None, total_offset, packets), length
        else:
            assert(length_type_id == 1), length_type_id
            # If the length type ID is 1, then the next 11 bits are a number
            # that represents the number of sub-packets immediately contained by this packet.
            number_of_sub_packets = to_int(bits[7:7 + 11])
            print(f"{tabs}number_of_sub_packets: {number_of_sub_packets}")
            packets = []
            total_offset = 0
            for i in range(number_of_sub_packets):
                new_packet, offset = extract(bits[18+total_offset:], depth+1)
                # print(new_packet, offset)
                total_offset += offset
                packets.append(new_packet)
            sum_version += v
            return Packet(v,t, None, total_offset, packets), total_offset

def part1(hex_packet):
    global sum_version
    sum_version = 0
    bits = parse(hex_packet)
    packets, length = extract(bits)
    return sum_version

# assert(extract("110100101111111000101000") == (Packet(version=6, type=4, data=2021, length=None, sub_packets=[]), 21))
# assert(extract("11101110000000001101010000001100100000100011000001100000") == (Packet(version=7, type=3, data=None, length=33, sub_packets=[Packet(version=2, type=4, data=1, length=None, sub_packets=[]), Packet(version=4, type=4, data=2, length=None, sub_packets=[]), Packet(version=1, type=4, data=3, length=None, sub_packets=[])]),33))
# assert(extract("00111000000000000110111101000101001010010001001000000000") == (   Packet(version=1, type=6, data=None, length=27, sub_packets=[Packet(version=6, type=4, data=10, length=None, sub_packets=[]), Packet(version=2, type=4, data=20, length=None, sub_packets=[])]),27))

# assert(part1("8A004A801A8002F478") == 16)
assert(part1("620080001611562C8802118E34") == 12)
# assert(part1("C0015000016115A2E0802F182340") == 23)
# assert(part1("A0016C880162017C3686B18A3D4780") == 31)

