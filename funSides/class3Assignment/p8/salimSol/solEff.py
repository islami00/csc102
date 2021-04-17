array = [1,2,3,4,5,6]

print("even Numbers", "\tOdd Numbers")
for element in array:
    if (element % 2) == 0:
        print("\t",element)
    else:
        print("\t"*5,element)
