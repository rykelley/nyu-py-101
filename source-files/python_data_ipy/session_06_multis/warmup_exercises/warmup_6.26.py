# 6.26:  Using the file "revenue.csv", build a "summing"
# dictionary, a dict of floats -- in this review, you can
# begin by creating a dictionary that sums up the amount of
# revenue garnered from each state -- a dictionary with unique
# state keys paired with a float sum reflecting the sum of
# float values for that state in the file.  As we did with
# counting or summing dictionaries, remember that as your loop
# encounters each state, it must check to see if the state key
# already exists in the dictionary.  If it is new to the dict,
# it should be added with a value of 0.0.  Then the dict
# should add the float value to the value associated with that
# state in the dict.  Element access:  print the revenue found
# for New Jersey.

outer_dict = {}
fh = open('../revenue.csv')

for line in fh:
    company, state, revenue = line.split(',')

    # your code here


fh.close()

# Expected Output:

# {'NY': 133.16, 'NJ': 265.4, 'PA': 263.45}
# 
# 265.4

