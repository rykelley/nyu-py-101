# 6.24:  Loop through this dict of dicts printing each key as
# well as looping through each "inner" dict, printing all keys
# and values found.

# Note that you can use a comma within a print statement to
# print two items together (this introduces a space between
# items).

import runreport

dod = {
  'a':  {
    'zz': 1,
    'yy': 2
  },
  'b':  {
    'zz': 5,
    'yy': 10
  }
}

# Expected Output:

# a
#   zz 1
#   yy 2
# b
#   zz 5
#   yy 10

