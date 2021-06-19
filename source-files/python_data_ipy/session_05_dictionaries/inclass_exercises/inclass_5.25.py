# 5.25:  Trap a "bad dict key" error.  If the user's key can't
# be found in the dict, an error occurs -- test this by
# inputting a key of 'XXX'.  Once you have observed the
# exception and exception type, use a 'try/except' statement
# to trap the exception and instead print 'key does not
# exist'.  Make sure to put your 'try' block around just one
# line of code.

z = {'a': 1, 'b': 2, 'c': 3}

ukey = input('please enter a key:  ')

print(z[ukey])

# Sample program run:

# please enter a key:  XXX
# key does not exist

