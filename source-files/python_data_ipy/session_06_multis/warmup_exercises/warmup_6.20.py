# 6.20:  Build a list of lists:  continuing from the previous
# solution, inside the loop create an "inner list" of just the
# id, city and state, and instead of appending the id, append
# this 3-element list to outer_list.  After the loop ends,
# pretty-print the resulting list of lists (i.e.
# print(json.dumps(outer_list, indent=4)).  Element access:
# access the city of the first row (i.e., the 2nd element of
# 1st list) using a double subscript.

import json

outer_list = []
fh = open('../student_db_names.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, fname, lname, street, city, state, zip = line.split(':')

    # your code here


fh.close()

# Expected Output:

# [['jk43', 'Plainview', 'NY'],
#  ['ZXE99', 'New York', 'NY'],
#  ['jab44', 'New York', 'NY'],
#  ['ak9', 'Philadelphia', 'PA'],
#  ['ap172', 'New York', 'NY'],
#  ['JB23', 'Jersey City', 'NJ'],
#  ['jb29', 'Jersey City', 'NJ']]
# 
# Plainview

