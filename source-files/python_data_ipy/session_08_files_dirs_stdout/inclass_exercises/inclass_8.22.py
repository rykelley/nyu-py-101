# 8.22:  Trap a "bad directory" error.

# The below code attempts to list a directory specified by the
# user's input.  An existing directory should allow the
# program to loop through the items in that directory.  A non-
# existent directory should raise an exception.  Once you have
# observed this, use a 'try/except' statement to trap the
# exception and instead print 'directory not found'.  Make
# sure to put your 'try' block around just one line, and make
# sure to add an exit() to the end of the except: block so the
# program doesn't continue if the directory can't be found.
# (Note that in Jupyter Notebook you must use sys.exit() and
# that Jupyter will respond as if this is an error.)
# 
# Test for both correct directory (shown at top) and incorrect
# directory.

# existing directory name:  ../shakespeare

import os

uidn = input("name of directory to list: ")

uidpath = os.path.join('..', uidn)

items = os.listdir(uidpath)

for item in items:
    print(item)


# Expected Output:

# directory not found

