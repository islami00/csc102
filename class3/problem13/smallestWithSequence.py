s = None
dataSet = [1234, 12413, 354, 2, 22, 52524, 334234, 6335, 235, 34, 34, 43, 345, 343, 1234]
# i wonder what happens if one of the elements is a string, cuz that would cause an error in testing the condition
# itself

# i think is is used to check identity of booleans , or to test certain special states like none, or element of sequence
for element in dataSet:
    if s is None or element < s:
        s = element
print(s)
# i do this cuz when we finally exit the loop, the literal smallest has been found, instead of printing it as we
# find it

