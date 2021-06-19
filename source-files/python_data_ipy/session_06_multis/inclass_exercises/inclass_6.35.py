# 6.35:  Build a list of dicts.

# Opening and reading revenue.csv, build a list of dicts where
# each list item in the "outer" list is a dict, and each
# "inner" dict represents a row from the file (with keys
# 'name', 'state' and 'revenue').

fh = open('../revenue.csv')

for line in fh:
    line = line.rstrip()
    name, state, fval = line.split(',')
    fval = float(fval)


fh.close()

# Expected Output:

# [
#  {'name': "Haddad's", 'state': 'PA', 'revenue': 239.5},
#  {'name': 'Westfield', 'state': 'NJ', 'revenue': 53.9},
#  {'name': 'The Store', 'state': 'NJ', 'revenue': 211.5},
#  {'name': "Hipster's", 'state': 'NY', 'revenue': 11.98},
#  {'name': 'Dothraki Fashions', 'state': 'NY', 'revenue': 5.98},
#  {'name': "Awful's", 'state': 'PA', 'revenue': 23.95},
#  {'name': 'The Clothiers', 'state': 'NY', 'revenue': 115.2}
# ]

