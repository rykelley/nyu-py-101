# 9.15:  Write a function that validates its argument.

# Define function make_case(), which takes two arguments:
# text, a string to be modified, and case a string that must
# be either 'upper' or 'lower'.  If case is not one of these,
# the function should raise a ValueError exception.  Then
# based on the case argument, return the string uppercased or
# lowercased.

import runreport

# your function def here



greeting = 'Hello.'

x = case(greeting, 'upper')         # str, 'HELLO.'
print(x)

y = case(greeting, 'lower')         # str, 'hello.'
print(y)

z = case(greeting, 'middle')        # ValueError:  "middle" is not a valid argument:
                                    #              must be "upper" or "lower"

# Expected Output:

# HELLO.
# hello.
# ValueError:  "middle" is not a valid argument:  must be "upper" or "lower"

