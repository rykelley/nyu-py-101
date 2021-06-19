# 7.13:  Detect object type and raise TypeError.  Use the
# isinstance() function to see if the argument to this
# function is an integer.  If it isn't, raise your own
# TypeError exception.

def doubleit(arg):
    if not isinstance(arg, int):
        # your code here
    return arg * 2

x = doubleit('5')


