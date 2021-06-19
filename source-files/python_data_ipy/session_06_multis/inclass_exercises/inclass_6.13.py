# 6.13:  Looping through:  dict of dicts.

# Loop through each key in the dict and print the key and
# associated value (a dict).  Then instead of printing each
# dict, print the key and 'lname' value for each key.  Use
# 'for' with a dict subscript, but make sure to confirm the
# type of each item in your loop.

dod = {

    'ak23':  { 'fname': 'Ally',
               'lname': 'Kane' },

    'bb98':  { 'fname': 'Bernie',
               'lname': 'Bain' },

    'js7':   { 'fname': 'Josie',
               'lname': 'Smith' },

}



# Expected Output:

# ak23 Kane
# bb98 Bain
# js7 Smith

