inp = input("Enter a test name:\n")

if inp.lower() < "islam":
    print(inp,"comes before islam")
if inp.lower() == "islam":
    print(inp,"is same in order as")
if inp.lower() > "islam":
    print(inp,"comes after islam")

# this comparison is done based on alphabetical order, so less or greater works just like numbers as long as cap is same
# CAPS come before lows
# the comparison is done letter by letter too, like how we think of it logically
