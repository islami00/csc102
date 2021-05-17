fhand = open("../dummyFiles/nile.txt")
count = 0
for line in fhand:
    print(line.strip())
    count += 1
print("The number of lines in your file is",count)