# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #

    summe = 0
    for number in ar:
        summer += number
    return summe

def test_simpleArraySUm():
    assert simpleArraySum([1,2,3]) == 6, simpleArraySum([1,2,3])
    assert simpleArraySum([100,200,50]) == 350, simpleArraySum([100,200,50])
    assert simpleArraySum([1, 10, 100, 2, 20, 200, 3000]) == 3333, simpleArraySum([1, 10, 100, 2, 20, 200, 3000])

    if __name__ == '__main__':
        test_simpleArraySUm()
        print("SUCCESS")