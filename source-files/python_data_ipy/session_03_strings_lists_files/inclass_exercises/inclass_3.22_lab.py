# 3.22:  Loop through file and sum up selected value.

# Looping through revenue.csv, sum up the float value (3rd
# field) only for those rows from NJ (2nd field).

import runreport

fname = '../revenue.csv'

fh = open(fname)

for line in fh:
    line = line.rstrip()


# Expected Output:

# 265.40

