# 5.9:  Starting with this list of non-unique values:

cities = ['Boston', 'Chicago', 'New York', 'Boston', 'Chicago',
          'Boston']

# Count the occurrence of each value in the list by compiling
# a count of cities in the dict:  store the city as a key in
# the dict and set or increment an integer count for the
# number of times that city occurred.  However, don't attempt
# to loop through the list more than once.  Hint:  as your
# loop encounters each element in the list, use the in
# membership test to see if the value is a key in the dict.
# If it isn't, add it as a key with a value of 0.  Then, still
# in the block, and whether or not it is in the dict, add one
# to the value for that key, and assign the new +1 value back
# to the dict for that key.

# Expected Output:

# {'Boston': 3, 'Chicago': 2, 'New York': 1}

