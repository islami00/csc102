# get file name and open and initiate dictionary,
# to be converted to sorted list of tuple of dictionary key/value pairs

print("Ensure file is in same folder as script!")
fName = input("Enter name of file")
fHand = open(fName, "r")
preses = dict()
presesSort = list()

for line in fHand:
    # get president name which is basically the line minus the first word
    presidentName = line.replace(line.split()[-1], "").strip()
    # get the country, which is the last word of the line
    country = line.split()[-1].strip()
    # update the dictionary with the new president's name, leaving same if president repeated
    preses[presidentName] = preses.get(presidentName, country)

# move president and details to the list
for president, country in preses.items():
    presesSort.append((country, president))

# sort list in ascending order of country name
presesSort.sort()

# print the sorted presidents and details in same format as input
for country, president in presesSort:
    print(president, country)
# for actual table output: check sol1ext, based on the output he gave us tho, this is what he wants
