fPath = input("Enter complete path to fil:\n")
fhand = open(fPath,"r")

for line in fhand:
    print(line)