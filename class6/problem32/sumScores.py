fPath = input("Enter complete path to fil:\n")
fhand = open(fPath,"r")
sum = 0
for line in fhand:
    line = line.strip()
    sum += int(line)
print(sum)
