fhand = open("../dummyFiles/nile.txt")
count = 0
for line in fhand:
    if not (("the" in line) or ("The" in line)):
        print(line)  # prints only lines without the