# 6.33:  Review:  build a dict from file.

# Opening and reading revenue.csv, build a dict of company
# names (the first value on the line) paired with revenue
# values (the last value on the line))

fh = open('../revenue.csv')

for line in fh:
    line = line.rstrip()
    name, state, fval = line.split(',')
    fval = float(fval)


fh.close()

# Expected Output:

# {"Haddad's": 239.5, 'Westfield': 53.9, 'The Store': 211.5,
#  "Hipster's": 11.98, 'Dothraki Fashions': 5.98,
#  "Awful's": 23.95, 'The Clothiers': 115.2}

