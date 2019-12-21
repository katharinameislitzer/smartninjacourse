def multiplication(number_1: int, number_2: int) -> int:
    result = number_1 * number_2
    return result


def difference(number_1, number_2):
    result = number_1 * number_2
    return result

    if result >=0:
        return result
    else:
        return -result


assert multiplication(5, 2)==10, multiplication(5, 2)
assert difference(2, 5)==10, difference(2, 5)
assert difference(-2, 5)==-10, difference(-2, 5)
assert difference(2, -5)==-10, difference(2, -5)
assert difference(0, 0)==0, difference(0, 0)
print("SUCCESS!")