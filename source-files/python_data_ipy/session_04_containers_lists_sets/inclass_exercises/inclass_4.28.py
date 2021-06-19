# 4.28:  Build a set of items from a CSV file.

# Loop through the file revenue.csv and create a set of states
# drawn from the 2nd column of the file.

fh = open('../revenue.csv')

states = set()       # the only way to initialize an empty set

for line in fh:
    items = line.split(',')


fh.close()

print(states)

# Expected Output:

# {'PA', 'NY', 'NJ'}

# Note:  your set may display in any order.

