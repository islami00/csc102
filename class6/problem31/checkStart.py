fhand = open("../dummyFiles/nile.txt")
count = 0
for line in fhand:
    if line.startswith("Nile") or line.startswith("NILE"):
        print(line)