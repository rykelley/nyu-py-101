# 9.16:  Write a function with an optional argument.

# Modify the above function so that the 2nd argument is
# optional, with default 'upper'.  Make sure it behaves as
# shown when called as shown below.

import runreport

# your function def here


greeting = 'Hello.'

a = make_case(greeting, case='lower')     # str, 'hello.'
print(a)

b = make_case(greeting, case='upper')     # str, 'HELLO.'

c = make_case(greeting)                   # str, 'HELLO.'
print(c)

d = make_case(greeting, case='title')     # ValueError:  "title" is not a valid argument:
print(d)                                  #              must be "upper" or "lower"

# Expected Output:

# hello.
# HELLO.
# HELLO.
# ValueError:  "title" is not a valid argument:  must be "upper" or "lower"

