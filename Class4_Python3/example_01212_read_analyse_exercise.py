# open the file "height.txt"
# it contains the height of each person in the class
# save its content as a list
# find out what the average height is

# Hint 1: you cannot use json here
# Hint 2: Here is some code that calculates the average of a list
list = ["1", "2", "3", "4", "5", "6"]
avg = 0
for i in list:
    avg += int(i)
avg = avg / len(list)
print("The average of list is:", avg)
