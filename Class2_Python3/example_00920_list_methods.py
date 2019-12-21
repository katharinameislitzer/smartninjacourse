a_list = []
b_list = [1, 2, 3, 4]

# append
b_list.append(5)
print(b_list)  # [1, 2, 3, 4, 5]

# remove
b_list.remove(3) #stoppt beim ersten 3er, den es findet und removt ihn
print(b_list)  # [1, 2, 4, 5]
# extend
b_list.extend([0, 77, 99]) #  elemente hinzufügen
print(b_list)  # [1, 2, 4, 5, 0, 77, 99]
b_list += [100, 101] # definiert zwischen Listen so wie concatonate, ähnlich wie extend
print(b_list)  # [1, 2, 4, 5, 0, 77, 99, 100, 101]
