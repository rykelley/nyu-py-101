# 9.17:  Write a function with both positional and optional
# arguments.

# Write function temp_convert() that takes one required
# argument temp, a temperature value, and an optional argument
# scale=, which must be 'C' or 'F', and a default value of
# 'C'.  If scale is not 'C' or 'F', the function raises a
# ValueError.
# 
# Formula for F->C:  (x − 32) * 5/9
# Formula for C->F:  (x * 9/5) + 32
# 
# Make sure the function behaves as shown below with the below
# arguments.

import runreport

# your function def here



c = temp_convert(212, scale='C')       # 100
print(c)

f = temp_convert(0, scale='F')         # 32
print(f)

cc = temp_convert(32)                  # 0
print(cc)

ff = temp_convert(-1, scale='Fahrenheit')   # ValueError:  "Fahrenheit" is not a
                                            # valid argument:  must be "C" or "F"
print(ff)

# Expected Output:

# 100
# 32
# 0
# ValueError:  "Fahrenheit" is not a valid argument:  must be "C" or "F"

