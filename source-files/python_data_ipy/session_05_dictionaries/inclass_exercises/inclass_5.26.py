# 5.26:  Trap a "bad list index" error.   If the user's index
# can't be found in the list, an error occurs -- test this by
# inputting an index of 9.  Once you have observed the
# exception and exception type, use a 'try/except' statement
# to trap the exception and instead print 'no value at that
# index'.  Make sure to put your 'try' block around just one
# line of code.

x = ['a', 'b', 'c', 'd']

uidx = int(input('please enter an index:  '))

print(x[uidx])

# Sample program run:

# please enter an index:  9
# no value at that index

