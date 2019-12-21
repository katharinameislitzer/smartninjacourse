# Schreibe eine while Schleife
# sie bricht nur dann ab, wenn der User "yes" oder "no" eingegeben hat

answer = None
while answer not in("yes", "no"):
    answer = input("Please enter answer: ")
else:
    print("Thank you")