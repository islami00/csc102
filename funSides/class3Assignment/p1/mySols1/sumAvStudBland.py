# approach two, dynamic entry, one by one using counter for logic test, and sum var for sum
# only compatibility issue is append

# initialise list and counters/sums

ages = []
i = 0
s = 0
# no error check

# max input test is in for loop
# for loop is ideal here cuz no need for err check; finite;
for i in range(5):
    # attach new age and count and sum
    ages.append(int(input("Enter age:")))
    s += ages[i]
    i += 1


average = float(s / i)
print(s, average)
