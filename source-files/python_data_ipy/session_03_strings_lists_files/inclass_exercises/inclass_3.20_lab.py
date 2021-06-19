# 3.20:  Loop through file and selectively print using
# split().

# Looping through revenue.csv, print the company names for
# rows with 'NY' as the state.

import runreport

filename = '../revenue.csv'

fh = open(filename)

for line in fh:
    # your code here


# Expected Output:

# Hipster's
# Dothraki Fashions
# The Clothiers

