freqTable = dict()
names = ["the boy", "the boy", "te", "ta", "ta", "te", 1, 1, 2, 2, 31, 41, 414, 41, 14, 241, 4, 11, 4124, 1412, 414]
# heh, numbers are easier to randomly bring out for me.

for dataValue in names:
    if dataValue not in freqTable:
        freqTable[dataValue] = 1
    else:
        freqTable[dataValue] += 1

print(freqTable)

# can also be used to tell number of words, lines and then occurrence of specific words
# NOTE: HE SAID THIS IS A GOOD EXAM QN.
# How are dictionaries ordered?? How do they remember placement of values without indexes??
