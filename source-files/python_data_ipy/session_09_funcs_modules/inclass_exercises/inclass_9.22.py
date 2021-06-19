# 9.22:  Import a variable from a module into the program's
# namespace.

# Perform the same as above but import a variable from
# 'mymod.py' directly into this program's namespace.  You
# should be able to print this variable without prepending the
# name with mymod or mm.  Again, print one of the varibles.

import sys

sys.path.append('../lib')    # temporary - puts mymod.py's diretory
                             #             in your import path

# your import and code here

