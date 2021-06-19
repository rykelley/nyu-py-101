# 3.23:  File line iteration and summary.

# Use 'for' to loop through file 'revenue.csv' and count the
# number of iterations, then perform the operations noted
# below:  test each step as you proceed.

filename = '../revenue.csv'
fh = open(filename)

counter = 0
summer = 0.0

# 1. loop through file line-by-line; strip and print each line

    # 2. count each iteration; print count at end

    # 3. split each line on a comma; print each split line

    # 4. subscript float value from split list; print each subscripted value

    # 5. convert float value (a string) to float

    # 6. sum up float values; print sum after loop ends

    # 7. adding a horizontal bar to separate iterations
    print('------------------------------')


# close file


# print sum and count


# Expected Output:

# Haddad's,PA,239.50
# 
# ["Haddad's", 'PA', '239.50\n']
# 239.50
# ------------------------------
# Westfield,NJ,53.90
# 
# ['Westfield', 'NJ', '53.90\n']
# 53.90
# ------------------------------
# The Store,NJ,211.50
# 
# ['The Store', 'NJ', '211.50\n']
# 211.50
# ------------------------------
# Hipster's,NY,11.98
# 
# ["Hipster's", 'NY', '11.98\n']
# 11.98
# ------------------------------
# Dothraki Fashions,NY,5.98
# 
# ['Dothraki Fashions', 'NY', '5.98\n']
# 5.98
# ------------------------------
# Awful's,PA,23.95
# 
# ["Awful's", 'PA', '23.95\n']
# 23.95
# ------------------------------
# The Clothiers,NY,115.20
# 
# ['The Clothiers', 'NY', '115.20\n']
# 115.20
# ------------------------------
# 7
# 662.0100000000001

