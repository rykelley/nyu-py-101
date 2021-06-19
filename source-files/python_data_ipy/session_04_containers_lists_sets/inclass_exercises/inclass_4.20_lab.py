# 4.20:  Compile a list of values from file lines.

# Build a list of student ids (first field) from
# student_db.txt.
# 
# See comment below for how to skip header.

import runreport

filename = '../student_db.txt'

fh = open(filename)

next(fh)             # skip the first line of the file

for line in fh:

    line = line.rstrip()

    items = line.split(':')



# Expected Output:

# ['jk43', 'axe99', 'jab44', 'ak9', 'ap172', 'jb23', 'jb29']

# Note:  don't forget that student_db.txt is colon-separated.

