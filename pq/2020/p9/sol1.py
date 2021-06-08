# a: open file in append mode to add FCTs gpa
fHand = open("listOfCGPAs.txt", "a")
fHand.writelines("\nFCT : 4.0")
# close then reopen the file to count the gp
fHand.close()
fHand = open("listOfCGPAs.txt", "r")
# assuming the cgpa are each on a separate line:
lines = list(fHand)
# fls is the float count (or gps if you wish) I DUB THEE SEPARATE FLOAT COUNTER!
fls = []

"""
so, explaining my logic for sol1: basically i figured out that GPs are decimals and
decimals are numbers separated by a "."
in the context of the file, the decimal is a word assuming it is space separated from everything else.
thus leaving me with the logic, for every line in the file, and every word in that line, split it based on a "."
if all parts of the word are numeric, it is decimal , and thus it is a GP.
this is true regardless of how the GPs are stored in the file as long as: 1.
"""

# b : for loop for gp count, assuming they aren't all on newlines

for line in lines:
    # extracts the GPAs if and only if they are space separated from others on the line
    for word in line.split():
        parts = ""
        for wPart in word.split("."):
            parts = parts + wPart
        # parts concatenates the parts of the decimal to avoid false positives
        if str(parts).isnumeric():
            fls.append(word)

fls = list(map(float, fls))
SumGp = sum(fls)
count = len(fls)

# easiest assumption. Converting from string to float directly is difficult.
# I DID IT THO! <The new hill is if the gpa is surrounded by special chars>

# C
average = round(SumGp / count, 2)
print(average)

fHand.close()

# D : can be defined in one line, because we were not asked to write to it
# the output for response in b is the number of gps, while the output for the response in c is the average gp
oFile = open("numAndAvgCGPA.txt", "w")

# E:
# if they are all on the same python file then i don't need to reopen an outfile
oFile.write("Number of CGPAs: " + str(count) + "\nAverage CGPA: " + str(average))
