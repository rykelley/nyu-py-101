""" 
get_FF_avg.py -- show average value of a particular
                 factor at a particular year in the 
                 Fama-French daily file 
"""

import sys


FACTOR_LIST = ['Mkt-RF', 'HML', 'SMB', 'RF']

SOURCE_FILENAME = 'FF_tiny.txt'


def usage(msg):
    """ prints error message and usage string, and exits """

    print(f'ERROR:  {msg}')
    exit(f'Usage:  {sys.argv[0]} [year] [factor]')


def validate_input():
    """ reads from input
        validates and returns year and factor
        calls usage() if incorrect """

    if len(sys.argv) != 3:
        usage('2 args required')

    year = sys.argv[1]
    factor = sys.argv[2]

    if not year.isdigit() or len(year) != 4:
        usage('first arg must be a 4-digit year')

    if factor not in FACTOR_LIST:
        usage(f'2nd arg must be one of {FACTOR_LIST}')

    return year, factor


def get_factor_list(year, factor):

    """ read file, parse out list of values
        from selected factor at selected year 
        returns list of values """

    values = []

    fh = open(SOURCE_FILENAME)
    lines = fh.read().splitlines()
    wanted_lines = lines[6:-2]

    for line in wanted_lines:

        if not line[0:4] == year:
            continue

        items = line.split()
        print(FACTOR_LIST.index(factor))
        factor_val = items[FACTOR_LIST.index(factor) + 1]

        values.append(float(factor_val))

    return values


# MAIN BODY CODE

year, factor = validate_input()

print(year, factor)
exit()

factors = get_factor_list(year, factor)

if not factors:
    exit('no values found')

avg = sum(factors) / len(factors)

print(f'{len(factors)} values, average {round(avg, 2)}')


