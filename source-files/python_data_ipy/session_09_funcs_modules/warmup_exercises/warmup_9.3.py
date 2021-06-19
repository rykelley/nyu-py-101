# 9.3:  Modify the above function to include an optional
# argument.  If name=[something], print hello, [something]!
# instead of hello, world!  But if the name= parameter is not
# passed, revert to saying hello, world!

# So your def hello function code will be modified to accept
# the name=text argument (i.e., def hello(name=False)), and
# then test to see if text has a value -- if it is True (i.e.,
# if name: is True).  If it is True, print it after 'hello, '.
# If it doesn't, print 'hello, world!'

import yourname

yourname.hello()                # hello, world!
yourname.hello(name='Python')   # hello, Python!

