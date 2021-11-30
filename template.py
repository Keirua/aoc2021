import argparse

def get_options():
    description = "Generates a template"
    argparser = argparse.ArgumentParser(description=description,
                                        formatter_class=argparse
                                        .RawTextHelpFormatter)
    argparser.add_argument('-d', '--day', type=int, default=1)
    argparser.add_argument('-y', '--year', type=int, default=2021)

    options = argparser.parse_args()

    return options

def get_template(day, year):
    return """import aoc
import re
import pprint

input = aoc.input_as_string(aoc.challenge_filename({day}, {year}))

lines = aoc.input_as_lines(input)
print(lines)
"""

if __name__ == '__main__':
    options = get_options()
    tpl = get_template(options.day, options.year)

    print(tpl)
