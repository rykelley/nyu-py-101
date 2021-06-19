# 5.16:  Build a "lookup" dict from row values in a CSV file.

# Looping through revenue.csv, build a dict with the company
# name as string key and the revenue number as float value.

corev = {}

fh = open('../revenue.csv')

for line in fh:
    company, state, rev = line.split(',')     # multi-target assignment


fh.close()

print(corev)

# Multi-target assignment allows us to assign multiple values
# from a list at one time.  The above code depends on each
# line having 3 items; otherwise the variables on the left
# would not match the number of items from the split() on the
# right.

# Expected Output:

# {"Haddad's": 239.5, 'Westfield': 53.9, 'The Store': 211.5,
#  "Hipster's": 11.98, 'Dothraki Fashions': 5.98, "Awful's": 23.95,
#  'The Clothiers': 115.2}

