# Notes: I'm missing some input validation making sure it's a number and not a string
# Also i'm showing some class errors with "Unresolved reference 'float'" for example
# this is also not PEP compliant it would seem




food_charge = float(input('Enter amount of money for the food: '))  # Input the total food bill and convert to
                                                                    # float

num_party = int(input('How many people in your party ?: '))          # This takes the input of integer for
                                                                     # the number of people in the party

tip = int(input('Please enter the desired tip percentage (for example,"20" for 20%: '))  # this takes the input of integer for the tip amout percentage

tip_total = "%.2f" % float (tip / 100 * food_charge)  # this formats the tip amount to show a
                                                      # percentage and turns that into a float
                                                      # of tip / by 100 for tip percentage * the food bill

total_bill = food_charge * float(tip / 100 + 1)       # this computes the total bill
                                                      # from food_charge and the
#                                                     # tip from the tip input

amount_each = (round(float(((tip / 100 + 1) * food_charge) / num_party), 2))  # this function takes base tip
                                                                              # percentage and * it by the food_charge
                                                                              # and then divides that output by number
                                                                              # in the party

print("\n")      # prints an extra blank line for readability

print(f"A {tip}% tip (${tip_total}) was added to the bill, for a total of ${total_bill}")     # takes the tip input

print("\n")      # prints an extra blank line for readability

print(f"With {num_party} in your party, each person must pay:  ${amount_each}")     # Shows the number is the party plus
                                                                                    # the food charge and tip for
                                                                                    # each person in the party divided equally
