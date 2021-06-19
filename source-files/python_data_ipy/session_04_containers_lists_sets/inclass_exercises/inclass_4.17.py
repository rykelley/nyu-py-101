# 4.17:  Build a list of items from a CSV file.

# Begin by reviewing and running the below code.  Taking a
# look at file revenue.csv, build up a list of the float
# values in that file.

fh = open('../revenue.csv')

fvals = []

for line in fh:
    line = line.rstrip()
    items = line.split(',')
    print(items)


fh.close()

# Expected Output:

# [239.5, 53.9, 211.5, 11.98, 5.98, 23.95, 115.2]

