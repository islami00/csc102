# this is the ultimate inputter, able to receive the 4 needed inputs by the split constraint
def getscore():
    n = list(map(int, input().strip().split()))
    while len(n) > 4:
        n.__delitem__(-1)
    return n

def addscore(arr):
    return sum(arr)


def display(arr):
    return addscore(arr) / len(arr)


b = getscore()
print(b)
print(addscore(b), display(b))
