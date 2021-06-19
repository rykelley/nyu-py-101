# 8.2:  Validate Arguments.  Extend the previous program to
# validate user input.  Using try: and except:, trap an
# IndexError exception if one of the two arguments is missing
# - and have the program exit() with a Usage: string if the
# exception occurs (see output and note below).

# Exceptions:  trap an exception for missing arguments
# (IndexError when reading from sys.argv).  (Remember to place
# as little code as possible in your try: block.)   If
# possible, print the program name in the Usage string (as
# shown below) using sys.argv[0].

# Expected Output:

# $ python myprog.py
# Usage: myprog.py [int1] [int2]
# 
# $ python myprog.py 5
# Usage: myprog.py [int1] [int2]
# 
# $ python myprog.py 5 hello
# Usage: myprog.py [int1] [int2]
# 
# $ python myprog.py 5 10
# 5 + 10 = 15

