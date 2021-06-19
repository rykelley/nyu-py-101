# 6.36:  Build a dict of dicts.

# Opening and reading revenue.csv, build a dict of dicts where
# each "outer" dict key is the name from the line, and each
# value is another dict.  The "inner" dict should have the
# remaining values from the row, with keys 'state' and
# 'revenue').

fh = open('../revenue.csv')

for line in fh:
    line = line.rstrip()
    name, state, fval = line.split(',')
    fval = float(fval)


fh.close()

# Expected Output:

# {"Haddad's": {'state': 'PA', 'revenue': 239.5},
#  'Westfield': {'state': 'NJ', 'revenue': 53.9},
#  'The Store': {'state': 'NJ', 'revenue': 211.5},
#  "Hipster's": {'state': 'NY', 'revenue': 11.98},
#  'Dothraki Fashions': {'state': 'NY', 'revenue': 5.98},
#  "Awful's": {'state': 'PA', 'revenue': 23.95},
#  'The Clothiers': {'state': 'NY', 'revenue': 115.2}}

