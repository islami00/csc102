s = 0
dataSet = [1234, 12413, 354, 2, 22, 52524, 334234, 6335, 235, 34, 34, 43, 345, 343, 1234]

for element in dataSet:
    s += element
# to avoid undefined case,separate count and avg from sum loop
count = len(dataSet)
avg = s/count
print(avg)
