# print(input(str("Welcome to buzzfizz, please enter a number between 1 and 100")))
def fizzbuzz_line(num: int) -> str:
    # write your code here
    result = num
    if num % 3 == 0 and num % 5 == 0:
        result = "fizzbuzz"
    elif num % 3 == 0:
        result = "fizz"
    elif num % 5 == 0:
        result = "buzz"
    return str(result)

def test_fizzbuzz_line():
    assert fizzbuzz_line(1) == "1"
    assert fizzbuzz_line(3) == "fizz"
    assert fizzbuzz_line(5) == "buzz"
    assert fizzbuzz_line(15) == "fizzbuzz"
    assert fizzbuzz_line(-3) == "fizz"

if __name__ == '__main__':
    test_fizzbuzz_line()
    for i in range(200):
        print(fizzbuzz_line(i))