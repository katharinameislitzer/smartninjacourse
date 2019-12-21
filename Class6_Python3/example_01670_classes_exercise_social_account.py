# create classes for social account
# they have a field for: name, friends
# they have methods to: count_friends, befriend, unfriend

class SocialAccount:  # Graph (object) muss man bei python 3 nicht mehr dazuschreiben
    def __init__(self, name): #  freunde noch nicht, weil wissen wir noch nicht
        self.name = name
        self.friends = [] # muss nicht unbedingt in init funktion sein

    def befriend(self, friend_account):  # (Susi, Hans) geht von unten rauf und holt befriend, wenn mans unten verwendet.
        self.friends.append(friend_account)
        friend_acount.friends.append(self)  #self ist eigene Instanz  -befreunden geht in beide richtungen

    def unfriend(self, friend_account):
        self.friends.remove(friend_account)
        friend_acount.friends.remove(self)

    def count_friends(self):
        return len(self.friends) #len weil liste von freunden ist

    def describe(self):
        print(self)

    def __str__(self):
        return f"{self.name} has {self.count_friends()} friends."

def test_count_friends():

if __name__ == '__main__':
    hans = SocialAccount("Hans")
    susi = SocialAccount("Susi")
    helmut = SocialAccount("Helmut")
    hans.befriend(susi)
    hans.befriend(helmut)
    hans.describe()  # sagt, wieviel freunde er hat
    susi.describe()
    susi.unfriend(hans)
    hans.describe()
    susi.describe()
    print(hans)
    assert hans.count_friends() == 2
    assert susi.count_friends() == 1