print(str(1))
print(type(1)) # <type = str>

eingabe_1 = "1"
eingabe_2 = "2"

print(3 + 4) #  int
print(eingabe_1 + eingabe_2)  # concat 12
print(int(eingabe_1) + int(eingabe_2)) #  3
print(float(eingabe_1) + float(eingabe_2)) # 3.0

resultat_1 = int(eingabe_1) + int(eingabe_2) # 3
resultat_2 = float(eingabe_1) + float(eingabe_2) #3.0
print(resultat_1, resultat_2)  #3 3.0

print(resultat_1 == resultat_2)  # true, das gleiche, nicht das selbe
print(resultat_1 is resultat_2)  # false
print(1 is 1)  # true
