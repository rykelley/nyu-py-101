import random           # import random function

num_random_gen = random.randint(1, 100)         # create random number

num_tries = 0           # Set number of tries counter to 0
num_guess = int(input("Guess a Number between 1 and 100: "))            # take input from user
while True:

    if num_guess > num_random_gen:          # First condition of the while loop
        print("Try a lower number")
        num_guess = int(input("Guess a Number between 1 and 100: "))        # takes input again
        num_tries += 1                      # keeps track of the first condition

    elif num_guess < num_random_gen:        # next condition  of the loop
        print("Try a higher number")
        num_guess = int(input("Guess a Number between 1 and 100: "))
        num_tries += 1

    else:                                   # if the user guess then while loop exits
        print("You got it !")
        break
if num_guess == num_random_gen:             # Last condition prints your number of tries and prompts to exit
    num_tries += 1
    print(f"you guessed it in {num_tries}")

    input('Press the enter key to exit')
    exit()
