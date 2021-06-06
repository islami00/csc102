# known: array
array = [7, 7, 7, 6, 8, 7]
# values: int, even, odd
# i was about to check if ends in
# check : occurrence of even, then odd
# divisible by 2 means mod 2 is zero


ax = array
evenTest = False
oddTest = False
# when the "trip" booleans arent in the for, they are triggered when the condition is and forever stay like that
for x in ax:
    if x % 2 == 0:
        evenTest = True
    else:
        oddTest = True

evenOnly = evenTest and not oddTest  # even does not imply odd, i.e when even is while odd isn't, then the
# implication is
# false, the one condition we want
# works from implication logic table

oddOnly = oddTest and not evenTest

evenAndOdd = not (evenOnly or oddOnly)  # could also be: evenTest or oddTest
# either: print indexes of even no.s and those of odd no.s

# or: count no. of evens, then those of odds

# tells you if both even and odd digits in array
print("EvenOnly", evenOnly, "oddOnly", oddOnly, "Both evenAndOdd", evenAndOdd)

# find both even and odd digits in each number
