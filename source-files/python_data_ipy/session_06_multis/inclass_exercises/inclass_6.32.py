# 6.32:  Review:  build a list from file.

# Opening and reading revenue.csv, build a list of float
# values from the file.

fh = open('../revenue.csv')

for line in fh:
    line = line.rstrip()
    name, state, fval = line.split(',')
    fval = float(fval)


fh.close()

# Expected Output:

# [239.5, 53.9, 211.5, 11.98, 5.98, 23.95, 115.2]

