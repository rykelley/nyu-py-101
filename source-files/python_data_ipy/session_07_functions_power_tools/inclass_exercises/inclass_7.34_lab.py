# 7.34:  Supreme Challenge!.

# Write a list comprehension that returns the list of lines
# with only the last name uppercased.
# 
# (Splitting the line, you can uppercase the first element,
# make a list out of it, append it to the list of remaining
# values, and use ','.join() with the list to reconstitute the
# comma-separated values.)

import runreport

lines = [  '2014-03-09,Wilson,Joe,Acme Inc.',
           '2014-08-17,Fink,Bart,Beta LLC',
           '2018-09-03,Emerson,Will,Acme Inc.',
           '2020-12-09,Rodgers,Mary,Gamma Co.',
           '2014-07-01,Jones,Pete,Acme Inc.'
        ]



# Expected Output:

# ['2014-03-09,WILSON,Joe,Acme Inc.', '2014-08-17,FINK,Bart,Beta LLC',
# '2018-09-03,EMERSON,Will,Acme Inc.', '2020-12-09,RODGERS,Mary,Gamma Co.',
# '2014-07-01,JONES,Pete,Acme Inc.']

