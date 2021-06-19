# 9.4:  Create a function getlines(filename) that takes a
# filename, opens the file for that filename, copies the lines
# of the file (i.e.from the file method .readlines()) to a
# list variable, and then returns the list.  In the calling
# code, call the function with a known filename, and assign
# the return value of the call to a variable.  Loop through
# the variable (of course it is a list) and print out each
# line in the file.

# your code here

lines = getlines('student_db.txt')

for line in lines:
  print(line)             # prints each line in file

