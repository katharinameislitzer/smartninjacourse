
# printe zahlen bis 100

# wenn die zahl gerade: print "yu"
# sonst wenn du zahl ungerade und größer 50: print "yo"
# sonst wenn du kleiner 20 print: "ye"
# sonst print die zahl

# 2->yu
# 51 -> yo
# 19 -> ye
# 35 -> 35

for number in range(1, 101):
    if number % 2 == 0:
        print("yu")
    elif number % 2 != 0 and number > 50:  # man müsste hier die ungeraden nicht extra anführen
        print("yo")
    elif number < 20:
        print("ye")
    else:
        print(number)