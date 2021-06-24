file = open("myTxt.txt", "r")
file = list(file)

f = open("out.txt", "w")
f.write("")
f.close()
for line in file:
    f = open("out.txt", "a")
    f.write("\n")
    f.close()
    for word in line.split():
        f = open("out.txt", "a")
        f.write(f"\n {word}")
        f.close()
