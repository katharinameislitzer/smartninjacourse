# write a list with the ingredients salad, orange, mango
# choose randomly an ingredient, and write it to a file called "random_fruit.txt"
import random
ingredients = ["salad", "orange", "mango"]  # Liste erstellen
random_ingredient = random.choice(ingredients)  # Liste mit neuer variable verrandomen mit random.choice

with open("ingredients.txt","w") as f: # Liste normal öffnen.
    f.write(random_ingredient)