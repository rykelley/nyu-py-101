# 7.12:  Raise an exception.  Test to see if the user's input
# matches one of the values in the valid_choices list (use if
# uchoice not in valid_choices).  If not, raise a ValueError
# exception.

def validate(uchoice):
    valid_choices = ['buy', 'sell', 'hold']
    if uchoice not in valid_choices:
        " raise a ValueError exception here "

    # return 1, 2 or 3 based on choice
    idx = valid_choices.index(uchoice) + 1

    return idx


choice = input('please enter an action ("buy", "sell", "hold"): ')

index = validate(choice)

print(f'action index is {index}')

