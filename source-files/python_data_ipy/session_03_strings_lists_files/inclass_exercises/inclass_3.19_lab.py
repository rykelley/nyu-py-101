# 3.19:  Loop through file and sum up values in column.

# Looping through datafile.csv, sum up the last column of
# float values.  Print the sum at the end.

import runreport

fname = '../datafile.csv'

fh = open(fname)

for line in fh:
    line = line.rstrip()
    # your code here


# Expected Output:

# 9.0

