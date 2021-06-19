# 8.18:  Trap a "bad index" error.   The below code takes user
# input and converts to int, then attempts to read the list
# item at that index value.  A correct index (0-3) should
# allow you to print the value at that index.  An incorrect
# index (>3) should raise an exception.  Once you have
# observed this, use a 'try/except' statement to trap the
# exception and instead print 'no value at that index'.  Make
# sure to put your 'try' block around just one line of code.

x = ['a', 'b', 'c', 'd']

uidx = int(input('please enter an index:  '))

print(x[uidx])


# Expected Output:

# please enter an index:  4
# no value at that index

