# the importation is extra for readability, int only already implemented
from typing import List


def max_even(even_ints: List[int]):
    # empty for evens
    evn = []
    # check each number
    for number in even_ints:
        # int only spec
        if type(number) != int:
            return "Value Error, list contains non-integers"
        # even test
        if number % 2 == 0:
            evn.append(number)
    # None spec
    if len(evn) == 0:
        return None
    # output max
    else:
        return max(evn)


print(max_even([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]))
print(max_even([3, -1001]))
