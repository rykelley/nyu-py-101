# 6.37:  Build a dict of lists.

# Opening and reading revenue.csv, build a dict of lists where
# each "outer" dict key is a state, and each value is a list
# of revenue values found on the same line as that state.

fh = open('../revenue.csv')

for line in fh:
    line = line.rstrip()
    name, state, fval = line.split(',')
    fval = float(fval)


fh.close()

# Expected Output:

# {'PA': [239.5, 23.95], 'NJ': [53.9, 211.5],
#  'NY': [11.98, 5.98, 115.2]}

