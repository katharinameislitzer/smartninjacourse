# you have 2 numbers, 5 and 10
# if the first is bigger than the second, print bigger
# if the second is bigger, print smaller
# otherwise print equal
smaller = 5
bigger = 10

if smaller > bigger:
    print(bigger)

elif bigger > smaller:
    print(smaller)

else: print("equal")


# you have a variable called "age"
# if age is smaller than 2, print baby
# if age is between 2 and 18, print kid
# otherwise print adult

age = 230
if age < 2:
    print("baby")
elif 2 <= age <= 18:
    print("kid")
elif age > 120:
    print("dead")
else:
    print("adult")