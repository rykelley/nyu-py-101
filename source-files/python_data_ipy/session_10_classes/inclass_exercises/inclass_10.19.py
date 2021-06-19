# 10.19:  Featured module:  zipfile.

import zipfile as zp

myzip = zp.ZipFile('myzip.zip', 'w')

# add names of files in the current directory
myzip.write()      # write 1st filename here
myzip.write()      # write 2nd filename here

myzip.close()

print('done')

# After running the above, check the session files directory
# -- you should see a new .zip file added.

