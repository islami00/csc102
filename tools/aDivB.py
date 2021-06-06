# divide list values
# This is just to automate operations on tables.
print("This code does first/second, so take note as you input for division\n")
a = list(map(float, input("Enter first list\n").strip().split(",")))
b = list(map(float, input("Enter second list\n").strip().split(",")))

# converts the data into 2d array of coordinates
coord = [list(a) for a in zip(a, b)]
tabOrNorm = int(input("Enter 0 for normal, 1 for tab separated\n"))

if tabOrNorm == 0:
    print("\nNormal values\n")
    for x, y in coord:
        print((coord.index(list((x, y))) + 1), x, y, round((x / y), 4))
else:
    print("\nTAB separated to export to excel\n")
    for x, y in coord:
        print(str(coord.index(list((x, y))) + 1), "\t", str(x), "\t", str(y), "\t", str(round((x / y), 4)))
