# 8.20:  Combine traps.  Place the try: block around both the
# input line and the list index line.  Now move your except:
# blocks so that they follow one another consecutively.  Test
# the program both with a bad integer value and a bad index,
# to see that either exception can be handled.

x = ['a', 'b', 'c', 'd']

try:
    uidx = int(input('please enter an index:  '))
except ValueError:
    print('numbers only, please')

try:
    print(x[uidx])
except IndexError:
    print('no value at that index')

# Sample program run:

# please enter an index:  4
# no value at that index

# Sample program run:

# please enter an index:  hello
# numbers only, please

