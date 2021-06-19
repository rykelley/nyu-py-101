# 8.23:  Command line only:  Identify error type and trap
# exception for missing command line argument.

# Suppose that the user has provided arguments at the command
# line resulting in sys.argv having the list values, as shown:

# command line argument:  1927
# 
# sys.argv value:          ['inclass_X.X.py', '1927']

# The program currently reads and prints the 1st command line
# argument ('1927', i.e. 2nd item of the list).  Now run the
# program without any argument and see what exception results.
# Then use a try/except to trap the error if it occurs.  If it
# does, print 'please enter an argument'.

import sys

arg = sys.argv[1]

print('argument is {arg}')

# Expected Output:

# please enter an argument

