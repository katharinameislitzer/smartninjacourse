# ask for a number to be inputted, and save it in a variable
# if the number is bigger than 1000, print You entered a very big number
# otherwise print The number is cute

number = input("Please enter a number: ")
number_2 = int(number)

if number_2 > 1000:
    print("You entered a very big number!")
else:
    print("The number is cute")