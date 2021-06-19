# 2.10:  Compare user input for a number to an integer for
# greater than or less than.

# Take keyboard input for a number from the user, then see if
# the number is greater than 0; if so, print 'positive'.
# Otherwise, see if it is less than 0; if so, print
# 'negative'.  Otherwise, print 'zero'.  Again, test with
# positive and negative values, and 0.  (Don't forget that if
# your logic says 'otherwise', it should use elif or else.)

import runreport

ui = input('please enter an int value: ')
ui_int = int(ui)
if ui_int > 0:
    print("positive")
elif ui_int < 0:
    print("negative")


