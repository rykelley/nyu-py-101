# 5.15:  Modifying the previous solution, allow the user to
# enter an argument indicating which direction the sort should
# go (the user can enter "ascending" or "descending").  Then
# using an if/else and testing the user's input, if
# "ascending", set a new variable rev to False; if
# "descending", set variable rev to True.  Finally, use this
# variable rev as part of the reverse argument, i.e.:

sorted_keys = sorted(mydict, key=mydict.get, reverse=rev)

# Sample program runs:

# please enter a direction:  ascending
# c => 0.3
# a => 5
# b => 7

# please enter a direction:  descending
# b => 7
# a => 5
# c => 0.3

# please enter a direction:  arskando
# enter "ascending" or "descending"

