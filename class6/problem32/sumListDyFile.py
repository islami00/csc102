fPath = input("Enter complete path to file:\n")
fhand = list(open(fPath,"r"))

for line in fhand:
    fhand[fhand.index(line)] = int(line.strip())
print(sum(fhand))
