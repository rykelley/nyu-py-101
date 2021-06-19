# 7.23:  Continuing the previous exercise, exclude the 1st
# line (the header line) from the output.  (Hint:
# file.readlines() returns a list of lines, and you can slice
# that list.  But since we can't assign open() to a
# filehandle, we can simply treat open() as if it were the
# filehandle (because it returns it); thus we can call the
# readlines() method on open(), and we can slice any list
# returned form a method, so we can attach a slice directly to
# the call to readlines().



# Expected Output:

# ['jk43:23 Marfield Lane:Plainview:NY:10023',
#  'ZXE99:315 W. 115th Street, Apt. 11B:New York:NY:10027',
#  'jab44:23 Rivington Street, Apt. 3R:New York:NY:10002',
#  'ak9:234 Main Street:Philadelphia:PA:08990',
#  'ap172:19 Boxer Rd.:New York:NY:10005',
#  'JB23:115 Karas Dr.:Jersey City:NJ:07127',
#  'jb29:119 Xylon Dr.:Jersey City:NJ:07127']

