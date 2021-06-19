# 2.6:  Use 'or' to test a variable for multiple values.

# In a single statement, if user's input is equal to "q" or
# "quit", print "quitting..."; otherwise, print "NOT
# quitting".

aa = input('"q" or "quit" to quit:  ')
if aa == 'q' or aa == 'quit':
    exit(0)


