import random

num_random_gen = random.randint(1, 100)

num_tries = 0
num_guess = int(input("Guess a Number between 1 and 100: "))
while True:

    if num_guess > num_random_gen:
        print("Try a lower number")
        num_guess = int(input("Guess a Number between 1 and 100: "))
        num_tries += 1

    elif num_guess < num_random_gen:
        print("Try a higher number")
        num_guess = int(input("Guess a Number between 1 and 100: "))
        num_tries += 1

    else:
        print("You got it !")
        break
if num_guess == num_random_gen:
    num_tries += 1
    print(f'you got it in {num_tries}')

input("\n\n Press the enter key to exit")
exit()
