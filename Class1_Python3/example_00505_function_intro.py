def subtraction(number_1: float, number_2: float) -> float:
    result = number_1 - number_2
    return result


def difference(number_1, number_2):
    result = number_1 - number_2      # damit kein Minus raus kommt, kann man if und else verwenden
    if result >=0:
        return result
    else:
        return -result

assert subtraction(12, 14)==-2, subtraction(12, 14)
assert difference(12, 14)==2, difference(12, 14)
assert difference(14, 12)==2, difference(14, 12)
assert difference(0, 0)==0, difference(0, 0)
print("SUCCESS!")





