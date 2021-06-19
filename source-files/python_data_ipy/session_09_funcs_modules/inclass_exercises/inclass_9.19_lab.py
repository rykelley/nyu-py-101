# 9.19:  Identify global and local variables.

# Identify the global and local names in the below code.
# There are 3 local and 4 global names to be identified.

import runreport

a = 5

def do(c, d):
    e = c * d
    return e

b = 100

x = do(a, b)       # 500
print(x)

