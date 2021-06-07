# no code, make mine
ls = [1, 2, 3, 1, 234, 234, 423, 424, 234, 24, 234, 23423]
es = []
# filtering evs
for number in ls:
    if number % 2 == 0:
        es.append(number)
print(max(es))
