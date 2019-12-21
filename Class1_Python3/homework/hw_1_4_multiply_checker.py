def multiplication(number_1: float, number_2: float) -> float:
    result = number_1 * number_2
    return result


def difference(number_1, number_2):
    result = number_1 * number_2
    return result


assert multiplication(5, 2)==10, multiplication(5, 2)
assert difference(2, 5)==10, difference(2, 5)
assert difference(0, 0)==0, difference(0, 0)
print("SUCCESS!")