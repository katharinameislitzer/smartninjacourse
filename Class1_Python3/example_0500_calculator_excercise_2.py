# print welcome to user
name = input("Please enter your name: ")
print(f"Welcome {name}")
# read user input for operation
operation = input("Please enter a mathematical sign (+, -, *, /): ")
print(f"You entered {operation}")
# read user input for first value
first_value = int(input("Please enter number one: "))
print(f"You entered {first_value}")
# read user input for second value
second_value = int(input("Please enter number two: "))
print(f"You entered {second_value}")
# calculate depending on operators

result = None

if operation is "+":
    print(f"The result is {first_value + second_value}")
elif operation is "-":
    print(f"The result is {first_value - second_value}")
elif operation is "*":
    print(f"The result is {first_value * second_value}")
elif operation is "/":
    print(f"The result is {first_value / second_value}")
else:
    print("nope, try again")
# and print result
