# 3.15:  Loop through file and print one field.

# Loop through datafile.csv and print just the first field
# from each line.

import runreport

filename = '../datafile.csv'

fh = open(filename)

for line in fh:
    # your code here

# Expected Output:

# this
# that
# this
# other
# something

