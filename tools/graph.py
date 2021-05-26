# any against any is Y against X
xAxis = list(map(float, input("Enter x-coordinates\n").strip().split(",")))
yAxis = list(map(float, input("Enter y-coordinates\n").strip().split(",")))
xScale = float(input("Enter x-axis scale\n").strip())
newXOrigin = float(input("Enter new x-axis origin\n").strip())
yScale = float(input("Enter y-axis scale\n").strip())
newYOrigin = float(input("Enter new y-axis origin\n").strip())
# nb: shift is like zero of function. shift center to right by a bit, negate a bit from prev center i.e take it as y=x
# same for y axis too
# I replaced shift with new origin cuz it is easier to understand, taking it like displacement, no matter how the shift
# is made, moving from x,y to the graph grid basically.

# converts the data into 2d array of coordinates
coord = [list(a) for a in zip(xAxis, yAxis)]

for x, y in coord:
    print((coord.index(list((x, y))) + 1), x, y, round(((x / xScale) - newXOrigin), 3), round(((y / yScale) - newYOrigin), 3))
# could expand this to an actual graphing software, already have the first half which is changing the coord to grid
