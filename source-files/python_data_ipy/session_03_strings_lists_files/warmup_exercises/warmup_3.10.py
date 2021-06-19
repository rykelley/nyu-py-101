# 3.10:  building on the previous program, now add the 'year
# selection' functionality from earlier and print only the 2nd
# column values whose lines match the year '1928'.

# Note on efficiency:  when adding in this functionality, you
# should make the line splitting and column selecting happen
# only if the year from the line is 1928.  This means that the
# loop block will start with the slicing, then the 'if' test
# asking if the slice is equal to 1928, then inside that 'if',
# splitting the line, selecting the 2nd column, and printing
# the 2nd column value.  The reason we want to follow this
# order is because we want the program to do as little work as
# possible:  there's no point in splitting the line or
# selecting the value if the year doesn't match -- we'll be
# ignoring those lines anyway.



# Expected Output:

# 0.43
# 0.14
# 0.71
# 0.25
# 0.44
# 1.12
# 0.23
# 0.07
# 0.49

