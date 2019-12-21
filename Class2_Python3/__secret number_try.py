secret_number = 5
guess= None

while guess != secret_number:
    guess = int(input("Please guess the secret number: "))

    if guess == secret_number:
         print("You have guessed the secret number")
    else:
        print("Sorry, the secret number is not " +  str(guess))