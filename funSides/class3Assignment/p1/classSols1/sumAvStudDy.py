s = 0
c = 0

# i added ageName for detail
ageName = ["first", "second", "third", "fourth", "fifth"]

while c < 5:
    age = int(input("Enter the " + ageName[c] + " age:"))
    s += age
    c += 1

print("The sum of the class age is:", s)
print("The average of the class age is:", s / c)
