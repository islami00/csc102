fhand = open("../dummyFiles/nile.txt")
count = 0
for line in fhand:
    count += len(line)
print("There are",count,"characters in the document")
