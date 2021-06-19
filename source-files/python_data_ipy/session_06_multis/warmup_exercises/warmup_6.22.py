# 6.22:  Build a dict of ids paired to states: inside the
# loop, add a key/value pair to outer_dict:  the id paired
# with the state.  Once the loop is done, print the dict.
# Then print the value for key ak9.

outer_dict = {}
fh = open('../student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')


fh.close()

# Expected Output:

# {'ak9': 'PA',
#  'ap172': 'NY',
#  'ZXE99': 'NY',
#  'jab44': 'NY',
#  'JB23': 'NJ',
#  'jb29': 'NJ',
#  'jk43': 'NY'}
# 
# PA

