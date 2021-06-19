# 8.28:  A function to generate a file listing.

# Write a function get_listing() that takes a directory name
# and returns the list of entries in that directory.  If the
# directory name is not a valid directory, have the function
# raise a NotADirectoryError exception.
# 

import runreport

# your function def here



# this should succeed
listing = get_listing('.')      # list, files and dirs in this dir
print(listing)
print()


# this should raise NotADirectoryError exception
listing = get_listing('wrong')
      # NotADirectoryError:  directory "wrong" could not be opened

