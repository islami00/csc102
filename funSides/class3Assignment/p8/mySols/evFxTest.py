def even_test(a):
    if int(a) % 2 == 0:
        return True
    else:
        return False


# that returns false if odd

arr = [111, 2134, 134, 1341, 141, 413413, 4134, 134, 134, 1414, 134, 14, 1]


def even_odd_array_tester(a):
    even_result = set({})
    for i in a:
        if even_test(i) is True:
            even_result.add(1)
        else:
            even_result.add(0)
    # miracle of set: no repeated elements
    if even_result == {1}:
        return "all even"
    elif even_result == {0}:
        return "all odd"
    elif even_result == {0, 1}:
        return "all even and odd"


print("the numbers in array are:", even_odd_array_tester(arr))

print("for each digit:")

for j in arr:
    print(j, "is", even_odd_array_tester(str(j)))
