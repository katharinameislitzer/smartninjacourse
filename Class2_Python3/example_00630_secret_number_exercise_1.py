# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt


secret = "7"
guess = 0
counter = 0

while True:
    counter += 1
    guess = input("Guess the secret number")

    if guess == secret:
        print("Oh, so great!, you won!")
        break
    elif counter > 5:
        print("You Lost! attempts: ", counter)
        break
    else:
        print("Oh no, please try again.attempts: ", counter)

