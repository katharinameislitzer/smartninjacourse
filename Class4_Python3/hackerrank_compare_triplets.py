

def compareTriplets(a, b):              #funktion, wos kein return gibt ist immer none
    alice_points = 0
    bob_points = 0
    n_games =  len(a)
    for i in range(n_games):
        if a[i] > b[i]:
            alice_points +=1
        elif a[i] < b[i]:
            bob_points += 1
    return [alice_points, bob_points]


    return [1, 1]                 #Lückenfüller, sorgt nur dafür dass keine Fehler angezeigt werde

def test_compareTriplets():
    assert compareTriplets([1, 2, 3], [3, 2, 1]) == [1, 1], compareTriplets([1, 2, 3], [3, 2, 1])
    assert compareTriplets([2, -1, 2], [0, -2, 0]) == [3, 0], compareTriplets([2, -1, 2], [0, -2, 0])
    assert compareTriplets([100, -50, 10.5], [20000, 100, 10.51]) == [0, 3], compareTriplets([100, -50, 10.5])

if __name__ == '__main__':
    test_compareTriplets()