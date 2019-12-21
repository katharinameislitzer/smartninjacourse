# save the following list in a file
# using one of the methods discussed previously
continents = ["Asia","Africa","North America","South America","Antarctica","Europe","Oceania"]

import json

with open ("continens.txt", "w") as f:
    f.write(json.dumps(continents))