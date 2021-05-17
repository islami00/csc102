fPath = input("Enter complete path to input:\n")
fhand = list(open(fPath,"r"))

for line in fhand:
    fhand[fhand.index(line)] = int(line.strip())
print(sum(fhand))
oPath = open(input("Enter complete path to output file:\n"),"w")
oPath.write(str(sum(fhand)))
# this competely overwrites the file with new content
