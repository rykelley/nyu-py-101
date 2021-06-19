# 9.12:  Raise an exception.  Test to see if the user's input
# matches one of the values in the valid_choices list (use if
# uchoice not in valid_choices).  If not, raise a ValueError
# exception with a descriptive error message.

def validate_choice(uchoice):

    valid_choices = ['run', 'stop', 'rewind']

    if uchoice not in valid_choices:
        # your code here


validate_choice('run')           # should have no visible effect - function did not raise

validate_choice('fastforward')   # should raise ValueError with a message

