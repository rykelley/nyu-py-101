# 5.20:  Build a dict from file.

# Looping through student_db_names.txt below, build up a dict
# of student ids to last name.  Print the dict.

import runreport

fname = '../student_db_names.txt'

fh = open(fname)
next(fh)

for row in fh:

    stuid, fname, lname, address, city, state, stuzip = row.split(':')



# Expected Output:

# {'jk43': 'Kane', 'axe99': 'Everbooty', 'jab44': 'Brillo',
#  'ak9': 'Krumpet', 'ap172': 'Perillo', 'jb23': 'Boto',
#  'jb29': 'Best'}

