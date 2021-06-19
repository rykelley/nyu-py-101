# 9.20:  Import a module and use its variables.  Import module
# 'mymod' (located in the 'lib' directory) and print one of
# its variables.

import sys

sys.path.append('../lib')    # temporary - puts mymod.py's directory
                             #             in your import path

# your import and code here

