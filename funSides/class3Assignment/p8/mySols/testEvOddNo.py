arr = [1, 2, 3, 45, 6, 67, 78, 8, 887, 7, 6, 6, 6, 67, 7, 7]

# this can be expanded for the array , this is the even, oddOnly, and evenAndOdd Test
for c in arr:
    evenAndOddTest = False
    evenTest = False
    oddTest = False
    con = str(c)
    for x in con:
        if int(x) % 2 == 0:
            evenTest = True
        else:
            oddTest = True
        if evenTest and oddTest is True:
            evenAndOddTest = True
            evenTest = False
            oddTest = False
    print(c, "evenAndOdd:", evenAndOddTest, "even:", evenTest, "odd:", oddTest)
