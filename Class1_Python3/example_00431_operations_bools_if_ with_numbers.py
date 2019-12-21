y = 4
# die erste Bedingung muss ein "if" sein!
if y > 5: # vergisst den Doppelpunkt nicht!
    print("smaller") # vergisst dem Einzug nicht! einfach auf "tab" druecken
elif y < 4: #elif steht fuer "else if". Ist die erste Bedingung nach "if" wahr, wird geprueft ob diese Bedingungen wahr ist.
    print("bigger")
elif y == 5: #man kann mehrere elif Bedingungen aufstellen
    print("equal")
else: #wenn keine von den vorigen Bedingungen wahr ist, wird "else" ausgeführt.
    print(" y ist 4!")


y = 5

if y > 5:
    print("zu groß")
elif y < 5:
    print("zu klein")
elif y == 5:
    print ("Goldylocks")
else:
    print("fünf isses")
