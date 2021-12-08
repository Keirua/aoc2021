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
lines = aoc.as_lines(input)
# lines = aoc.as_lines(example_input)

print(lines)
def n_on(signals, n):
    return list(filter(lambda s: len(s) == n, signals))

nb_1478 = 0

for l in lines:
    signals, output_value = l.split(" | ")
    signals = list(map(lambda s: sorted(s), signals.split(" ")))
    output_value = list(map(lambda s: sorted(s), output_value.split(" ")))

    two_on = n_on(signals, 2)[0]   # number 1
    three_on = n_on(signals, 3)[0] # number 7
    seven_on = n_on(signals, 7)[0] # number 8
    four_on = n_on(signals, 4)[0]  # number 4
    mapping = {
        "".join(two_on): 1,
        "".join(three_on): 7,
        "".join(four_on): 4,
        "".join(seven_on): 8
    }
    pp.pprint(mapping)
    for o in output_value:
        if o in [two_on, three_on, four_on, seven_on]:
            nb_1478 += 1
    six_on = four_on = n_on(signals, 6)

print(nb_1478)
