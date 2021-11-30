from typing import List
import argparse
import datetime


def get_current_year() -> int:
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    return year

def get_yd_options(cli_description: str = ""):
    """
    :param cli_description: the description that appears on the command line
    :return:
    Generates an ArgumentParser with the year and day options set
    """
    argument_parser = argparse.ArgumentParser(description=cli_description, formatter_class=argparse.RawTextHelpFormatter)
    argument_parser.add_argument('-d', '--day', type=int, default=1)
    argument_parser.add_argument('-y', '--year', type=int, default=get_current_year())

    return argument_parser.parse_args()


def challenge_filename(day: str, year: str) -> str:
    """
    :param day: day number, 1 to 25
    :param year: year
    :return: the name of a challenge file
    """
    return f"input/{day}_{year}.txt"


def input_as_string(filename: str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")


def as_lines(s: str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return s.split("\n")


def as_ints(lines: List[str]) -> List[str]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))
