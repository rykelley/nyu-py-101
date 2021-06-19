# 8.5:  List a Directory.  Accept a string argument that is
# the pathname of a directory.  Print out all items in the
# directory listing using os.listdir().  Trap the exception
# that would result from an unreadable directory (i.e., if not
# exist or no permissions.  To determine this exception, try
# to read a directory that doesn't exist, and note the
# exception that results).  Using os.path.isfile(listing) and
# os.path.isdir(listing), where listing is one of the items
# returned from listdir(), identify whether the listing is a
# file or directory.

# Note that while listdir returns filenames, it doesn't return
# file paths.  So if the directory you're listing isn't in the
# same directory as your Python program, you'll need the whole
# path.  You can construct a whole path and test a file this
# way:

filepath = os.path.join(dir, filename)

# so you can do a file test this way:

if os.path.isfile(os.path.join(dir, filename)):

# Exceptions:  trap exception for missing argument (IndexError
# when trying to access sys.argv[1]) and unreadable directory
# (OSError when attempting to read directory using
# os.listdir()).

# Program runs (output of course depends on the directory you
# supply):

# $ python myprog.py
# error:  please provide an argument
# 
# $ python myprog.py xxxxnonexistxxx
# error:  directory does not exist or is not readable
# 
# $ python myprog.py .       # '.' represents the current directory
# access_log.txt (file)
# ALL_DATA.zip (file)
# dormouse.html (file)
# ex3.txt (file)
# ... [etc.] ...

