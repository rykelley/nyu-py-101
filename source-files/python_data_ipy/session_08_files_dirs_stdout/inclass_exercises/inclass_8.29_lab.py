# 8.29:  A function to process command line arguments (test
# from command line only).

# Write a function get_args() that reads from sys.argv and
# returns the 2nd through last items in the sys.argv list
# (i.e., a slice omitting the first item).  If no arguments
# are passed at the command line, the function will return an
# empty list.
# 

import runreport

import sys

# your function def here



args = get_args()          # returns a list with 2nd through
                           # last items in sys.argv
print(args)

# You must of course run this program from the command line
# and pass arguments at the command line to see this program
# work properly.

