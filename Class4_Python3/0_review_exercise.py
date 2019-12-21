# read the data in the file hello.txt
# and print it in the terminal


hello = "hello.txt"                     #variable mit textfile
with open("hello.txt", "r") as f:       # textfile öffnen
    x = f.read                          # noch eine Variable mit f.read/write/append
print(x)                                # print