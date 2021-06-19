# 6.34:  Build a list of lists.

# Opening and reading revenue.csv, build a list of lists where
# each item in the "outer" list is a row, and each row is an
# "inner" list of values split from the line.

fh = open('../revenue.csv')

for line in fh:
    line = line.rstrip()
    name, state, fval = line.split(',')
    fval = float(fval)


fh.close()

# Expected Output:

# [["Haddad's", 'PA', 239.5], ['Westfield', 'NJ', 53.9],
#  ['The Store', 'NJ', 211.5], ["Hipster's", 'NY', 11.98],
#  ['Dothraki Fashions', 'NY', 5.98], ["Awful's", 'PA', 23.95],
#  ['The Clothiers', 'NY', 115.2]]

