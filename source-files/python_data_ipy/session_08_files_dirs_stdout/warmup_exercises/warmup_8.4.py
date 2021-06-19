# 8.4:  Validate filename.  Continuing the previous program,
# take a filename from the user through the command line.  Use
# os.path.isfile() to see if the submitted file is an existing
# file (and not a directory or link or other entity).  If it
# is a file, then print the filename and size.  If it is not a
# file, then print an error message.

# Expected output (will vary depending on file chosen)

# $ python myprog.py student_db.txt
# student_db.txt:  333 bytes
# 
# $ python myprog.py xxxfile.txt
# error:  xxxfile.txt is not a file in this dir

