fhand = list(open("../dummyFiles/nile.txt"))
delim = None
add = 0
add2 = 0
for line in fhand:
    delim = [x for x in line if not x.isalnum()]
    delim = "".join(delim)
    delim = delim.split()
    print(delim)
    add2 += len(line.split())
    for character in line:
        for delimiter in delim:
            if delimiter == character:
                line = line.replace(character,"")
    add += len(line.split())

print("Actual, no symbol Word count is:",add)
print("Error word count with symbol is:",add2)