# lemme make this known: the max function checks the ascii code of each string element i.e every character, returning
# the one with the highest value.
# ascii code : starts at null, ends in del
# A is 41 , a is 61 , . is 60 , 0 is 30 , listed in order .

a = max("yo derondisimo how are you?")
b = max(1, 2, 324, 32, 235, 25235, 2525, 2235, 2525235, 252, 525, 25235, 5252, 525, 2535, 2352, 523, 252523, 53452525,
        252, 252)
c = min("Hello my lady hello my darling hello my ragtime gaaaalll")
d = min(-12, 14 - 1, 4 - 441, 41 - 4, 1, 41, 41 - 414 - 141, 4 - 141, 43, 13 - 5, 1 - 5, 13, -515, -1515, -151, -515, 1)
print(a, b, c, d)
