# 6.21:  Build a list of dicts:  modifying the previous
# solution, instead of an inner list, inside the loop create
# an "inner dict" of the id, city and state, keyed to string
# keys 'id', 'city' and 'state'.  Your "inner dict" should
# look like this:

inner_dict = {'id': id, 'city': city, 'state': state }

# Now append inner_dict to the outer list.  Once the loop is
# done, pretty-print the resulting list of dicts.  Element
# access: print Philadelphia from the 4th row.

import json

outer_list = []
fh = open('../student_db_names.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, fname, lname, street, city, state, zip = line.split(':')

    # your code here


fh.close()

# Expected Output:

# [{'city': 'Plainview', 'id': 'jk43', 'state': 'NY'},
#  {'city': 'New York', 'id': 'ZXE99', 'state': 'NY'},
#  {'city': 'New York', 'id': 'jab44', 'state': 'NY'},
#  {'city': 'Philadelphia', 'id': 'ak9', 'state': 'PA'},
#  {'city': 'New York', 'id': 'ap172', 'state': 'NY'},
#  {'city': 'Jersey City', 'id': 'JB23', 'state': 'NJ'},
#  {'city': 'Jersey City', 'id': 'jb29', 'state': 'NJ'}]
# 
# Philadelphia

