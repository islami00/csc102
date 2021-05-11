# any against any is Y against X
xAxis = list(map(float, input("Enter x-coordinates\n").strip().split(",")))
yAxis = list(map(float, input("Enter y-coordinates\n").strip().split(",")))
xScale = float(input("Enter x-axis scale\n").strip())
xfShift = float(input("Enter x-axis forward shift\n").strip())
yScale = float(input("Enter y-axis scale\n").strip())
yfShift = float(input("Enter y-axis forward shift\n").strip())
# nb: shift is like zero of function. shift center to right by a bit, negate a bit from prev center i.e take it as y=x
# same for y axis too.

# converts the data into 2d array of coordinates
coord = [list(a) for a in zip(xAxis, yAxis)]

for x, y in coord:
    print((coord.index(list((x, y))) + 1), x, y, ((x / xScale) - xfShift), ((y / yScale) - yfShift))
# could expand this to an actual graphing software, already have the first half which is changing the coord to grid
