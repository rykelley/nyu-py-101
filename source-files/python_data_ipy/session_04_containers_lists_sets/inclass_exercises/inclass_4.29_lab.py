# 4.29:  Show a set of unique cities in student_db.txt.

# You can begin by running the below code, which opens the
# file, advances one line, then loops through each line and
# splits the line.

import runreport

filename = '../student_db.txt'

fh = open(filename)
next(fh)

for line in fh:
    items = line.split(':')
    print(items)



# Expected Output:

# {'Plainview', 'Philadelphia', 'New York', 'Jersey City'}

# Note:  don't forget that student_db.txt is colon-separated,
# and that you must use next(fh) (where fh is the file object)
# to skip the header row of this file.

