# 7.15:  This list comprehension iterates over each line in
# the file (line for line in fh).  Apply .rstrip() to each
# line to produce a list of stripped lines.

fh = open('../revenue.csv')

lines = [ line for line in fh ]


fh.close()

