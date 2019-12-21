# Task 1

# define 2 variable and give them the values 2 and 10, then calculate the result of the division 2/10.
# print the result

# write your code here
x = 2
y = 10

result = x / y

print(result)


# Task 2

# save your first name and last name as string, and concat them to 1 variable,
# and print the result
x = "Kathi"
y = "Meislitzer"

ergebnis = x +" " + y

print(ergebnis)

# write your code here

# Task 3

# divide a number by 0, what happens?


# write your code here

# kann auch einfach nur die Zeile hinschreiben.Kann nicht durch 0 teilen!


try:
    1 / 0
    print("success")
except:
    print('tried to divide by zero, please stop')

print("Finished execution")