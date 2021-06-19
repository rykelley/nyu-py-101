# 3.13:  Loop through file and strip.

# Loop through the file pyku.txt and strip each line as you
# go.  You should see the lines printed without a blank line
# in between.

import runreport

filename = '../pyku.txt'

fh = open(filename)

for line in fh:
    # your code here

# Expected Output:

# We're all out of gouda.
# This parrot has ceased to be.
# Spam, spam, spam, spam, spam.

