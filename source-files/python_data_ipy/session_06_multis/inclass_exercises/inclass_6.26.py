# 6.26:  Trap a "missing file" error.  If the below file can't
# be found, Python will raise an exception.  First, allow the
# exception to occur and note the exception type as well as
# the line number.  Next, wrap the line in a try: block and
# follow with an except: block that notes the type.  In the
# except: block, print an error message that indicates that
# the file can't be opened, and then exit the program (in
# Jupyter Notebook, make sure to use sys.exit()).

import sys

filename = '../whatfiledoyoumean'

fh = open(filename)

for row in fh:
    print(row)

