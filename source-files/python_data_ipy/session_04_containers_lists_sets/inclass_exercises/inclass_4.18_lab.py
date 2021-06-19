# 4.18:  Review:  loop through a file.

# Open the below file, then use the next() function with the
# file object to skip the first line of the file.  Strip and
# print each line.

import runreport

filename = '../student_db.txt'

# open file


# skip the first line of the file (use next())


# loop through file line-by-line


    # strip each line


    # print each line



# Expected Output:

# jk43:23 Marfield Lane:Plainview:NY:10024
# axe99:315 W. 115th Street, Apt. 11B:New York:NY:10027
# jab44:23 Rivington Street, Apt. 3R:New York:NY:10002
# ak9:234 Main Street:Philadelphia:PA:08990
# ap172:19 Boxer Rd.:New York:NY:10005
# jb23:115 Karas Dr.:Jersey City:NJ:07127
# jb29:119 Xylon Dr.:Jersey City:NJ:07127

# Note that the header (id:address:city:state:zip) has been
# skipped with next().

