# when you have entered five numbers, program should halt
# sum any five added numbers
# the sum is initially zero and the count so we have to initialise the two

c = 0
s = 0
# the int is not so necessary given the operations
while int(c) < 5:
    x = int(input("Enter a number"))
    s = int(s) + x
    c += 1
print("The sum of the five numbers is", s)

# thinking about it, this would really simplify that sum problem , except they wanted two inputs

# if the inut isnt in the loop,, it adds the no. to itself five times
