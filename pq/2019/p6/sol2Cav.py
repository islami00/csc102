num = [1, 2, 3, 4, 46, 7, 7, 9, 10]


def even(arr):
    return list(filter(lambda x: x % 2 == 0, arr))


def not_in_arr(base_arr, filter_arr):
    return list(filter(lambda x: x not in filter_arr, base_arr))


print(max(even(num)))

print(max(not_in_arr(num, even(num))))
