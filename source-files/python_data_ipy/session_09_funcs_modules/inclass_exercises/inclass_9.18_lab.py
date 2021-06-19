# 9.18:  Write a function that returns multiple values.

# Define function name_split(), which takes a single string
# and attempts to split it on whitespace into 2 or 3 items.
# If there are more than 3 or fewer than 2 items, it raises a
# ValueError with a descriptive message.  If there are three
# items, it returns them; if there are two items, it returns
# the first item, None, and the second item.
# 
# Make sure the function return values are as shown below.

import runreport

# your function def here




first, second, third = name_split('George Patrick Flanahanahan')
print(first, second, third)      # 'George', 'Patrick', 'Flanahanahan'

fname, sname, tname = name_split('Aimee Vonda')
print(fname, sname, tname)       # 'Aimee', None, 'Vonda'

fn, sn, tn = name_split('Gimpy P. W. Simpson')
print(fn, sn, tn)                # ValueError:  must be 2 or 3 words in name

# Expected Output:

# George Patrick Flanahanahan
# Aimee None Vonda
# ValueError:  must be 2 or 3 words in name

