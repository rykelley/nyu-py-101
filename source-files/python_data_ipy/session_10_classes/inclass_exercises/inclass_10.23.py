# 10.23:  Featured module:  csv.

import csv

fh = open('../dated_file.csv')
reader = csv.reader(fh)

for row in reader:
    print(row)

fh.close()


# wfh = open('../newfile.csv', 'w', newline='')
# writer = csv.writer(wfh)

# writer.writerow(['a', 'b', 'c'])

# wfh.close()

# Again, please be advised that you will not see writes to a file
# until you close the file with fh.close() or until the program
# ends execution.  This is particularly critical with Jupyter as
# it is basically a running program.

