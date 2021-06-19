# 9.7:  Demonstration:  remove a return statement and note the
# value.

# The below function returns the sum of its arguments.  First
# run the program and note the printed value, then remove the
# return statement to see the printed value.

def get_sum(val1, val2):
    valsum = val1 + val2
    return valsum


r = get_sum(5, 10)
print(r)

