fHand = open("../../class6/dummyFiles/nile.txt")
count = dict()
for line in fHand:
    for word in line.split():
        count[word] = count.get(word, 0) + 1  # set the value to the previous value plus one ,
        # defaulting to zero if there isn't a previous value
sortList = list()

# put the words and their frequency in sort list
for k, v in count.items():
    sortList.append((v, k))

# sort in descending order
sortList.sort(reverse=True)
# Print the top ten values first, with some numbering to visualise the ranking using enumerate.
var = [print(f"{a + 1}. {b} {c}") for a, (b, c) in enumerate(sortList[0:10])]
# Then all the values after this next separator
print(f"{'-' * 15}")
for v, k in sortList:
    print(v, k)
print(count)

# List comprehension can be used too.
# this can be asked in a question. like: print the five top words in a paragraph or top 5 .
