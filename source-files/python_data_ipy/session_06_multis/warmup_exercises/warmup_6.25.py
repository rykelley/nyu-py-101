# 6.25:  Build a dict of lists (states):  modify the previous
# solution so that each state is associated with a list of ids
# for that state -- so you are building a dict that pairs each
# state with a list of ids.  You can do this very simply by
# replacing the integer 0 with an empty list, and the integer
# incrementing with a list append().  Element access:  loop
# through and print all the student ids for the students from
# New Jersey.

outer_dict = {}
fh = open('../student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')


fh.close()

# Expected Output:

# { 'NJ': ['JB23', 'jb29'],
#   'NY': ['jk43', 'ZXE99', 'jab44', 'ap172'],
#   'PA': ['ak9'] }
# 
# JB23
# jb29

