inFile = list(open("files/essay.txt", "r"))

secondLine = str(inFile[1])
print(secondLine)
wordsSecond = secondLine.split()
print("The words in the second line are:")

a = list(map(print, wordsSecond))

print("\nThe words in the second line that start with c are:")
c = [print(x) for x in wordsSecond if x.lower().startswith("c")]