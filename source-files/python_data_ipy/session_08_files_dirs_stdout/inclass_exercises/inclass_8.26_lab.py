# 8.26:  List a directory and identify file or directory.

# Modify the previous solution so that the program identifies
# each listing as either a file or directory.

import runreport

import os

dirname = '../testdir'

entries = os.listdir(dirnames)

for name in entries:
    fpath = os.path.join(dirname, name)
    print(fpath)

# Expected Output:

# ../testdir/file2.txt:  file
# ../testdir/file3.txt:  file
# ../testdir/testdir3:  dir
# ../testdir/testdir2:  dir

# In the above example, I am using an f'' strings to print the
# colon and file or dir after each entry.

