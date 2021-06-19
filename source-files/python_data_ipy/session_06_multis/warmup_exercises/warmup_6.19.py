# 6.19:  Build a list of ids:  inside a loop through
# student_db_names.txt, split the line and append each id to
# outer_list.  After the loop ends, print the list.  Then
# print the first element in the list.

import json

outer_list = []
fh = open('../student_db_names.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, fname, lname, street, city, state, zip = line.split(':')

    # your code here


fh.close()

# Expected Output:

# ['jk43', 'axe99', 'jab44', 'ak9', 'ap172', 'jb23', 'jb29']
# 
# jk43

