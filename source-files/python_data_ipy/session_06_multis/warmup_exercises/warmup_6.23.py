# 6.23:  Build a dict of dicts:  inside the loop, create an
# "inner dict" of street, city, state and zip.  Your "inner
# dict" should look like this:

inner_dict = { 'street': street, 'city': city,
               'state': state, 'zip': zip }

# Then, still inside the loop, add a key/value pair to
# outer_dict:  the id paired with the inner_dict.  Once the
# loop is done, pretty-print the resulting dict of dicts.
# Element access:  print the state for ak9.

outer_dict = {}
fh = open('../student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')


fh.close()

# Expected Output:

# {'JB23': {'city': 'Jersey City',
#           'state': 'NJ',
#           'street': '115 Karas Dr.',
#           'zip': '07127\n'},
#  'ZXE99': {'city': 'New York',
#            'state': 'NY',
#            'street': '315 W. 115th Street, Apt. 11B',
#            'zip': '10027\n'},
#  'ak9': {'city': 'Philadelphia',
#          'state': 'PA',
#          'street': '234 Main Street',
#          'zip': '08990\n'},
#  'ap172': {'city': 'New York',
#            'state': 'NY',
#            'street': '19 Boxer Rd.',
#            'zip': '10005\n'},
#  'jab44': {'city': 'New York',
#            'state': 'NY',
#            'street': '23 Rivington Street, Apt. 3R',
#            'zip': '10002\n'},
#  'jb29': {'city': 'Jersey City',
#           'state': 'NJ',
#           'street': '119 Xylon Dr.',
#           'zip': '07127\n'},
#  'jk43': {'city': 'Plainview',
#           'state': 'NY',
#           'street': '23 Marfield Lane',
#           'zip': '10023\n'}}
# 
# PA

