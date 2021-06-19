# 9.11:  Identify local and global variables.

# Identify the 3 local variables and 2 global variables in the
# below code:

filename = '../pyku.txt'

def get_text(fname):
    fh = open(fname)
    text = fh.read()
    return text

txt = get_text(filename)

