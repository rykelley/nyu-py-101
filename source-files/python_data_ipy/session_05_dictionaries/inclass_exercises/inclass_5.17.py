# 5.17:  Build a "counting" dict from a file.

# Again looping through revenue.csv, build a dict that counts
# how many states are in the 2nd column.

corevcount = {}

fh = open('../revenue.csv')

for line in fh:
    company, state, rev = line.split(',')     # multi-target assignment


fh.close()

print(corevcount)

# Expected Output:

# {'PA': 2, 'NJ': 2, 'NY': 3}

