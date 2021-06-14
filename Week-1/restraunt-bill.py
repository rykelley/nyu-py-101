
# Prompt user for the charge of the food


food_charge = float(input('Enter amount of money for the food: '))       # Input the total food bill and convert to float

num_party = int(input('How many people in your party ?: '))              # This takes the input of

tip = int(input('Please enter the desired tip percentage (for example,"20" for 20%: '))

tip_total = "%.2f" % float(tip / 100 * food_charge)

total_bill = food_charge * float(tip / 100 + 1)

amount_each = (round(float(((tip / 100 + 1) * food_charge) / num_party), 2))



print("\n")





print("\n")

print(f"A {tip}% tip (${tip_total}) was added to the bill, for a total of ${total_bill}")



print("\n")

print(f"With {num_party} in your party, each person must pay:  ${amount_each}")


