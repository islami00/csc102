def getscore ():
    a =[]
    while len(a) <4 :
        n = int(input())
        a.append(n)
    return a

def addscore(arr):
    return sum(arr)

def display(arr):
    return addscore(arr)/4

b = getscore()
print(addscore(b),display(b))