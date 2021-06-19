# 5.3:  Demo:  generate KeyError exception.

# Run the below program, entering a key in the dict.  Then
# enter a key that is not in the dict.  Note the exception
# type and message.

myd = {'a': 1, 'b': 2, 'c': 3}

ukey = input('please enter a key:  ')

print(myd[ukey])

