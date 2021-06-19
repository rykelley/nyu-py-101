# 6.31:  Identify and trap an exception (3).

# Run the program and allow the exception to happen.  Then
# wrap your try: block around the minimum # of lines and
# follow with an except: block that identifies the exception
# prints a warning.  (Remember not to use except: by itself or
# except Exception:.)

import runreport

countries = { 'USA': 328.2,
              'Canada': 37.59,
              'Mexico': 127.6  }

ukey = input('please enter a country name: ')

print(f'{ukey} population is {countries[ukey]}')

# Expected Output:

# Warning:  there was an error.

# Please note that we would normally do more than just say
# 'there was an error'.  Error messages need to be specific in
# order to alert the user to what happened or what they need
# to do in response.

