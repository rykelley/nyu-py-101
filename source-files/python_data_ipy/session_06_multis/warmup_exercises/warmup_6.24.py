# 6.24:  Build a "counting" dictionary, a dict of ints:  as a
# review, create a counting dictionary that counts the number
# of occurrences of each state -- a dictionary with unique
# state keys paired with an integer count reflecting the
# number of states in the file.  As we did with counting or
# summing dictionaries, remember that as your loop encounters
# each state, it must check to see if the state key already
# exists in the dictionary.  If it is new to the dict, it
# should be added with a value of 0.  Then the dict should add
# 1 to the value associated with that state in the dict.
# Element access:  print the number of students who are from
# New York.

outer_dict = {}
fh = open('../student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')


fh.close()

# Expected Output:

# {'NY': 4, 'NJ': 2, 'PA': 1}
# 
# 4

