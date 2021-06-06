inFile = open("../../class6/dummyFiles/nile.txt", "r")
words = list()
for line in inFile:
    for word in line.split():
        words.append(word)
print("The number of words is:", len(words))
# the main reason we didn't use the delimiter to remove special symbols is cuz they themselves are words! ms word
# pointed it out. Thus, the correct way is above, counting words
