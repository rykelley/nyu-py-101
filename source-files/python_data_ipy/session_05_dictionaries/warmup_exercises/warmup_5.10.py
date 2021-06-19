# 5.10:  Start with an empty dictionary.  Opening and reading
# student_db.txt, build a dictionary of states and a count for
# each state.  Print the dictionary.  Make sure to use only
# the dictionary to count -- no independent counting with an
# integer, list, etc.



# Expected Output:

# {'NY': 4, 'NJ': 2, 'PA': 1}

# Hint:  the key to making a counting dictionary work is in
# checking to see if any given key ito be counted is new to
# the dictionary.  If the key is new, it must be added to the
# dictionary.  If it isn't new, it will be rewritten to the
# dictionary, but with a new value that is (in this case) one
# more than the value it held earlier.  So consider the dict
# equivalent of this:

x = x + 1

# would only work if 'x' already exists

# Here is the dict equivalent:

mydict['x'] = mydict['x'] + 1

# would only work if key 'x' already exists

# where 'x' is a value that may appear multiple times in the
# data, and our object is to count it (as well as any other
# values that appear).
# 
# So, since we can't know whether any given key is new, we
# must check:

if 'x' not in mydict:

# Basically the simplest way to make this work is check to see
# if the key is new; if it is, set it in the dict with a value
# of 0.  Then, whether or not it is new, you can go ahead and
# add 1 to it - if it is new, the new value with this key will
# be 1.  If it is not new, this adding will simply increment
# the value.

