# Write a loop, which asks for an input,
# until you entered a valid operator

# hint:
# "+" in "+-/*" print("+-" in "+-/*")     # True
# "+" in ["*", "+", "-", "/"] print("+-" in ["*", "+", "-", "/"])  false

operator = None
while operator not in("+", "-", "*", "/"):
    operator = input("Please enter a valid operator: ")
else:
    print("Thank you")