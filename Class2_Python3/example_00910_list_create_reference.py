a_list = []

#  index  0  1  2  3 - index 0 verweist auf 1. element
b_list = [1, 2, 3, 4]
print(a_list)
print(b_list)

# reference
# print a_list[0]  # IndexError, because has no elements

print(b_list[-1])  # 4
b_list[1] = 10  #nummer 1 wird mit der nummer 10 überschrieben
print(b_list)
