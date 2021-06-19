# 2.9:  Compare user input for a number to an integer for
# equivalence.

# Take keyboard input for a number from the user, then see if
# the number is equal to integer 5.  If so, print 'is equal to
# 5'.  Again, test both with 5 and another value.

import runreport

test_int = 5

ui = input('please enter an int value: ')
ui_int = int(ui)
if ui_int == 5:
    print('is equal to 5')
elif ui_int > 5:
    print("Nope !")

