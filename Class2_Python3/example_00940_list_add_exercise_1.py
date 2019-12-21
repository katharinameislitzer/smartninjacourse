# take your shopping list, "bread", "butter", "chocolate"
# you are on a diet, and decide to remove "chocolate"
# print the list before and after removing
# instead, you will add "proteins"
# append it to your list, and print your list
# extra: try adding elements to the list by
# 1) adding (+)
# 2) extending
shopping_list = ["bread", "butter", "chocolate"]
print(shopping_list)
shopping_list.remove("chocolate")
print(shopping_list)
shopping_list.append("proteins")
print(shopping_list)
shopping_list.extend(["carrots"])
print(shopping_list)
shopping_list += ["apples"]
print(shopping_list)
