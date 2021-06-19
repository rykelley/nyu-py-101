# 9.9:  Explore function scoping.

# Call this function, then attempt to print lvar after calling
# the function.  Is lvar available outside the function?

def do(arg):
    lvar = arg * 2
    return lvar


a = do(5)
print(a)

