# 8.19:  Trap a "bad value" error.

# Since the input line also converts to int an input value
# that is not all digits should also raise an exception.  Once
# you have observed this, use a 'try/except' statement to trap
# the exception and instead print 'numbers, only please'.
# Make sure to put your new 'try' block around just one line
# of code.  Also, add an exit() to the except: block so the
# code doesn't continue executing past that line.  (Note that
# in Jupyter Notebook you must use sys.exit() and that Jupyter
# will respond as if this is an error.)

x = ['a', 'b', 'c', 'd']

uidx = int(input('please enter an index:  '))

try:
    print(x[uidx])
except IndexError:
    print('no value at that index')

# Expected Output:

# please enter an index:  hello
# numbers only, please

