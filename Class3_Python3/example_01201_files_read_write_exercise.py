# write a list with the ingredients salad, orange, mango
# choose one element of the list
# and write it to a file called "fruit.txt"

ingredients = ["salad", "orange", "mango"]   # liste erstellen


with open("fruits.txt", "w") as f:   # with open erstellt man dann ein file, schreibt w für write,
    f.write(ingredients[2])             # dann neue variable (f) erstellen und f.write(liste+[welches ingredient])


