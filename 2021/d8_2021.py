import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(8, 2021))
example_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
example2 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
lines = aoc.as_lines(input)
test_example2 = aoc.as_lines(example2)
test_lines = aoc.as_lines(example_input)

# print(lines)
def n_on(signals, n):
    return list(filter(lambda s: len(s) == n, signals))


def part12(lines):
    nb_1478 = 0
    sum_output_values = 0

    for l in lines:
        signals, output_value = l.split(" | ")
        signals = list(map(lambda s: sorted(s), signals.split(" ")))
        output_value = list(map(lambda s: sorted(s), output_value.split(" ")))

        number_1 = n_on(signals, 2)[0]   # only number 1 has 2 wires on
        number_7 = n_on(signals, 3)[0] # number 7
        seven_on = n_on(signals, 7)[0] # number 8
        four_on = n_on(signals, 4)[0]  # number 4
        mapping = {
            "".join(number_1): 1,
            "".join(number_7): 7,
            "".join(four_on): 4,
            "".join(seven_on): 8
        }

        for o in output_value:
            if o in [number_1, number_7, four_on, seven_on]:
                nb_1478 += 1
        # so there are 3 numbers with six wires on:
        # 0,6 and 9
        # the number 9 is the only number with 6 wires that one of the two wire of 1 off
        six_wires_on = n_on(signals, 6)
        assert(len(six_wires_on) == 3)
        possible_number_6 = list(filter(lambda s: number_1[0] not in s or number_1[1] not in s, six_wires_on))
        assert(len(possible_number_6) == 1)
        number_6 = "".join(possible_number_6[0])
        mapping[number_6] = 6

        # the number 9 is the only number with 6 wires that has the same wires as 4
        possible_number_9 = list(filter(lambda s: four_on[0] in s and four_on[1] in s and four_on[2] in s and four_on[3] in s, six_wires_on))
        # print(possible_number_9)
        assert (len(possible_number_9) == 1)
        number_9 = "".join(possible_number_9[0])
        mapping[number_9] = 9

        # 0 is the remaining 6-letters long wire
        sixes = list(map(lambda s: "".join(s), six_wires_on))
        number_0 = list(set(sixes) - set([number_6, number_9]))[0]
        mapping[number_0] = 0

        # now there are 3 digits with 5 wires: 2, 3, 5
        five_wires_on = n_on(signals, 5)
        five_wires_on = list(map(lambda s: "".join(s), five_wires_on))
        assert (len(five_wires_on) == 3)

        possible_number_3 = list(filter(lambda s: number_7[0] in s and number_7[1] in s and number_7[2] in s, five_wires_on))
        assert (len(possible_number_3) == 1)
        number_3 = possible_number_3[0]
        mapping[number_3] = 3
        five_wires_on = list(set(five_wires_on)-set([number_3]))
        assert (len(five_wires_on) == 2)

        # yeah, that sucks, lets pretend it works and call it a day
        if number_1[0] in five_wires_on[0]:
            if number_1[0] in number_6:
                number_5 = five_wires_on[0]
                number_2 = five_wires_on[1]
            else:
                number_5 = five_wires_on[1]
                number_2 = five_wires_on[0]
        else:
            assert(number_1[1] in five_wires_on[0])
            if number_1[1] in number_6:
                number_5 = five_wires_on[0]
                number_2 = five_wires_on[1]
            else:
                number_5 = five_wires_on[1]
                number_2 = five_wires_on[0]

        mapping[number_2] = 2
        mapping[number_5] = 5

        pp.pprint(mapping)
        for d in signals:
            if "".join(d) not in mapping:
                raise ValueError("missing mapping")
        output_value = list(map(lambda s: "".join(s), output_value))
        sum_output_values += int("".join([str(mapping[o]) for o in output_value]))

    return nb_1478, sum_output_values, mapping

_, sum_output_values_ex2, mapping = part12(test_example2)
print(sum_output_values_ex2)
assert(mapping["".join(sorted("acedgfb"))] == 8)
assert(mapping["".join(sorted("fbcad"))] == 3)
assert(mapping["".join(sorted("dab"))] == 7)
assert(mapping["".join(sorted("cefabd"))] == 9)
assert(mapping["".join(sorted("cdfgeb"))] == 6)
assert(mapping["".join(sorted("eafb"))] == 4)
assert(mapping["".join(sorted("cagedb"))] == 0)
assert(mapping["".join(sorted("ab"))] == 1)
assert(mapping["".join(sorted("cdfbe"))] == 5)
assert(mapping["".join(sorted("gcdfa"))] == 2)
assert(sum_output_values_ex2 == 5353)
nb_1478_test, sum_output_values_test, mapping_test = part12(test_lines)
assert(nb_1478_test == 26)
assert(sum_output_values_test == 61229)
nb_1478, sum_output_values, mapping = part12(lines)
assert(nb_1478 == 445)
print(nb_1478, sum_output_values)