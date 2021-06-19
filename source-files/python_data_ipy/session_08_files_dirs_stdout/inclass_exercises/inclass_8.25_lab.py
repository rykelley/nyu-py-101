# 8.25:  List a directory and show file sizes.

# Extend the previous solution by printing the file size of
# each file or directory.  Use a comma between varaible names
# to print two values on the same line, e.g. print(this,
# that).

import runreport

import os

dirname = '../testdir'

items = os.listdir(dirname)

for name in items:
    fpath = os.path.join(dirname, name)
    print(fpath)

# Expected Output:

# ../testdir/file2.txt 752
# ../testdir/file3.txt 200
# ../testdir/testdir3 160
# ../testdir/testdir2 128

