# 4.34:  Read a file as a list of string lines.

# Read 'revenue.csv' as a list of strings (use .readlines());
# print the list.  Then use a list slice to select only the
# 2nd through last lines of the file - print these as well.

filename = '../revenue.csv'

fh = open(filename)



# Expected Output:

# ["Haddad's,PA,239.50\n", 'Westfield,NJ,53.90\n',
#  'The Store,NJ,211.50\n', "Hipster's,NY,11.98\n",
#  'Dothraki Fashions,NY,5.98\n', "Awful's,PA,23.95\n",
#  'The Clothiers,NY,115.20\n']
# 
# ['Westfield,NJ,53.90\n', 'The Store,NJ,211.50\n',
#  "Hipster's,NY,11.98\n", 'Dothraki Fashions,NY,5.98\n',
#  "Awful's,PA,23.95\n", 'The Clothiers,NY,115.20\n']

