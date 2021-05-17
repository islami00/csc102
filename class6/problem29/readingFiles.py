# file handles are the data type or window to files
fhand = open("../dummyFiles/nile.txt")

for line in fhand:
    print(line)
# this prints it with the eofs or the newlines at the end and the newline created by the print function creating double
# space
