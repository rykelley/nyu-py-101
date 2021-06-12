#Prompt user for the charge of the food


food_charge = float(input('Enter amount of money for the food: ')) #This will convert the number entered into a float (so the user can type in 34.88, etc)
num_party = input('How many people in your party ?: ')
tip_party = input('Please enter the desired tip percentage (for example,"20" for 20%: ')

# configure tip amount

tip_multiplier = 20 / 100 # Assuming Tip is 20%
print("Your tip is: ", format(tip, '.0%'))

# total amount
total_amount = food_charge + tip_multiplier

amount_each = total_amount / num_party

print("Your total amount is: " , format(total_amount, '.2f'))