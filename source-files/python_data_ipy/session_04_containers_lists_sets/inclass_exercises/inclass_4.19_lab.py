# 4.19:  Review:  loop through a file and split out values.

# Continuing the previous exercise, split each line and print
# the list split from each line.

import runreport

filename = '../student_db.txt'

fh = open(filename)

next(fh)  # skip the first line of the file (use next())

for line in fh:

    line = line.rstrip()

    # your code here -- remember that this file is colon-separated



# Expected Output:

# ['jk43', '23 Marfield Lane', 'Plainview', 'NY', '10024']
# ['axe99', '315 W. 115th Street, Apt. 11B', 'New York', 'NY', '10027']
# ['jab44', '23 Rivington Street, Apt. 3R', 'New York', 'NY', '10002']
# ['ak9', '234 Main Street', 'Philadelphia', 'PA', '08990']
# ['ap172', '19 Boxer Rd.', 'New York', 'NY', '10005']
# ['jb23', '115 Karas Dr.', 'Jersey City', 'NJ', '07127']
# ['jb29', '119 Xylon Dr.', 'Jersey City', 'NJ', '07127']

