# 5.21:  Build a counting dict.

# Looping through revenue.csv below, build up a dict with
# state keys and a count of each state as values.   Print the
# dict.

import runreport

fname = '../revenue.csv'

fh =  open(fname)

for row in fh:
    name, state, amount = row.split(',')



# Expected Output:

# {'PA': 2, 'NJ': 2, 'NY': 3}

