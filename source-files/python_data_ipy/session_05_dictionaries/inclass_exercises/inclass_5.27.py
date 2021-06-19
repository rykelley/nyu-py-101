# 5.27:  Trap a "bad int value" error.  Add another except:
# block to the one below that will trap the exception that
# occurs if the user doesn't type a number.  If this exception
# is trapped, print 'please enter a number'.

x = ['a', 'b', 'c', 'd']

try:
    uidx = int(input('please enter an index:  '))
    print(x[uidx])
except IndexError:
    print('no value at that index')

# Sample program run:

# please enter an index:  hey
# please enter a number

