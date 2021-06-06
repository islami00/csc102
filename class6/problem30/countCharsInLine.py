fhand = open("../dummyFiles/nile.txt")
count = 0
for line in fhand:
    print(line.strip())
    print("This line contains",len(line),"characters")
# incls eof

# the file handle is taken as a sequence fof strings where each line in the file is a string in the sequence
