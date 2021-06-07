fHand = open("Nile.txt", "r")
lines = list(fHand)
words = []
lWords = []
eWords = []

# get words and lines
for line in lines:
    for word in line.split():
        words.append(word)

lenWords = len(words)

# get words starting with L and e
for word in words:
    if word.startswith("L"):
        lWords.append(word)
    if word.startswith("e"):
        eWords.append(word)
# print lines, words number and also the 3rd line

print(len(lines), lenWords, lines[2])

# print words starting with a, then e
for a in eWords:
    print(a)
for b in lWords:
    print(b)

# close file for second interpretation of line 3 qn
fHand.close()
# open in append mode
fHand = open("Nile.txt", "a")
# write stuff to the third line
fHand.writelines("awdadsda")
