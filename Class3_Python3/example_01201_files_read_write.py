text = "This is a new text now\n"

filename = "foo.txt"

# apart from reading a file you can also
# store data in it. This can be done by
# adding a parameter in the open() function.
# verschiedene modii:
# a : append -> will append at the end
# w : write -> will overwrite (clears the file), wenns file schon gibt, wird ganzes file überschrieben,
# r : read
# no parameter : automatically read

# the file is created automatically,
# once the open(..., "w") - function
# in writing mode is initiated 

# we can use the "with" keyword to simplify
# the file opening process
with open(filename, "a") as f: # name der variable, mit dem ich auf handler zufgreifen möchte- f is so wie my_file
    f.write(text + "more code please!\n")               # deswegen f.write - file muss nicht existieren, wenns nicht existiert, wirds so erstellt.

# the file is closed automatically after
# the "with" clause is over

print("FINISHED WRITING, START READING")

with open(filename, "r") as f:   # "r" für read
    content = f.read()   #  muss variable mitgeben, wos gespeichert wird.
    print(content)


print("Done")
