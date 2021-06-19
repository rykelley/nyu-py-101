# 6.27:  Build a dict of lists (floats):  modify the previous
# solution so that each state is associated with a list of
# revenue floats for that state -- so you are building a dict
# that pairs each state with a list of revenue values for the
# state.  You can do this very simply by replacing the float
# 0.0 with an empty list, and the float summing with a list
# append().  Element access:  provide the average company
# revenue for New York.

outer_dict = {}
fh = open('../revenue.csv')

for line in fh:
    company, state, revenue = line.split(',')

    # your code here


fh.close()

# Expected Output:

# { 'NJ': [53.9, 211.5],
#   'NY': [11.98, 5.98, 115.2],
#   'PA': [239.5, 23.95] }
# 
# 44.3866666667

