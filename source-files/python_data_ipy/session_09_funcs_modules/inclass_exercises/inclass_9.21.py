# 9.21:  Import a module as a different name and use its
# variables.  Perform the same as above but import the module
# as 'mm'.  Again, print one of the varibles from mymod.py.

import sys

sys.path.append('../lib')    # temporary - puts mymod.py's directory
                             #             in your import path

# your import and code here

