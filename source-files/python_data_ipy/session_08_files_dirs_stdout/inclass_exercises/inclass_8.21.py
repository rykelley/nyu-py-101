# 8.21:  Trap a "missing file" error.   The below code
# attempts to open a file specified by the user's input.  An
# existing filename should allow the program to show the
# length of the file in bytes.  A non-existent filename should
# raise an exception.  Once you have observed this, use a
# 'try/except' statement to trap the exception and instead
# print 'file does not exist'.  Make sure to put your 'try'
# block around just one line.

# existing filename:  ../pyku.txt

import os

uifn = input("enter filename to see size in bytes: ")

print(f"this file's length is {os.path.getsize(uifn)}")

# Expected Output:

# enter filename to see size in bytes: ../pyku.txt
# this file's length is 80

