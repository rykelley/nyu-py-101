


#Prompt user for the charge of the food


food_charge = float(input('Enter amount of money for the food: '))          #This will convert the number entered into a float (so the user can type in 34.88, etc)
num_party = int(input('How many people in your party ?: '))
tip = int(input('Please enter the desired tip percentage (for example,"20" for 20%: '))

tip_total = tip / 100

total_bill = food_charge * float(tip / 100 +1)

amount_each = (round(float(((tip / 100 + 1) * food_charge) / num_party), 2))

total_bill_float = float(total_bill)
tip_amount_float = float(tip_total)
tip_and_total = (total_bill_float+tip_amount_float)
print(f"Total bill including tip: ${tip_and_total}")

print("\n")

print(f"A {tip}% tip (${tip_total}) was added to the bill, for a total of ${tip_and_total}")



print("\n")

print(f"With {num_party} in your party, each person must pay:  ${amount_each}")


