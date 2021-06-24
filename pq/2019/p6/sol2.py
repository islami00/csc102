num = [1, 2, 3, 4, 46, 7, 7]


def max_even(arr):
    return list(filter(lambda x: x % 2 == 0, arr))


print(max_even(num))
