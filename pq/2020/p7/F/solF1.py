# no code, make mine
ls = [1,2,3,1,234,234,423,424,234,24,234,23423]
# I have to create a new list from ls using thels list function else es will just serve as a symlink for editing ls
es = list(ls)
# reverse direction, removing ods to create ev list from copy.
for number in es:
    if number % 2 != 0:
        es.__delitem__(es.index(number))
print(max(ls))