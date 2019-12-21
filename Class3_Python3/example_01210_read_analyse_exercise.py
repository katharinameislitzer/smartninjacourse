# open the file "height.txt"
# it contains the height of each person in the class
# save its content as a list
# find out what the average height is

with open("height.txt") as f:           # file öffnen
    list = f.read().split(",")             #lesen und als liste speichern

    av_hight=0              # variable f. average hight hier leer weil noch nicht benannt
    number_students=len(list)  #len returns number of items in an object
    for i in list:             # for Schleife. i muss vorher nicht definiert sein.
        av_hight +=(int)(i)

    av_hight = av_hight/number_students

    print(av_hight)