# 8.30:  Raise an exception if input is correct (command line
# only).

# Extend the previous solution to accept an argument, an
# integer.  The integer will specify how many arguments should
# be in sys.argv (not counting the initial filename argument
# of course).  If there are not the indicated number of
# arguments, the function will raise a ValueError exception.

import runreport

import sys

def get_args():             # add argument here
    args = sys.argv[1:]
    # add the size test and exception raising here

    return args


args = get_args(2)

# Expected Output:

# # if no arguments are passed
# args = get_args(2)              # ValueError('must pass 2 cmd args')
# 
# 
# # if two arguments are passed (this that)
# args = get_args(2)              # list, ['this', 'that']

