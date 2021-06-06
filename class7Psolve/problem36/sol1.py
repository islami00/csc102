inFile = list(open("files/essay.txt", "r"))

secondLine = inFile[1]
print(secondLine)
wordsSecond = secondLine.split()
print("The words in the second line are:")
for word in wordsSecond:
    print(word)
print("\nThe words in the second line that start with c are:")
for word in wordsSecond:
    if word.startswith("c"):
        print(word)
