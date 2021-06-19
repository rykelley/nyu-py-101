# 9.10:  Explore global variables inside functions.

# Replace 2 with gvar inside the function, then call the
# function.  Is gvar available inside the function?

gvar = 2

def do(arg):
    lvar = arg * 2
    return lvar


a = do(5)
print(a)

