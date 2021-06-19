# 5.8:  Given the following string:

personal_info = "595-33-9193:68:Columbus, OH"

# Split the data into a list of strings.  Then in a single
# statement insert it into a string so that it appears as
# shown in the output.  (Hint:  the easiest with is to use a
# triple-quoted f""" """ string (which may include newlines):

# print(f"""SS#: {}
# Age: {}
# Residence: {}""")   # fill these {} tokens with variables in the string

# or a single string with newlines (\n), i.e.

print(f"SS#: {}\nAge: {}\nResidence: {}")   # fill these {} tokens with variables in the string

# (in either example above, you would fill the {} tokens with
# the three items from the split)

# Expected Output:

# SS#:  595-33-9193
# Age:  68
# Residence:  Columbus, OH

