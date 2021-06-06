# find the 5th term of an ap wherein the tenth term is 5 and it is defined by the formula: T = T2 + 1

def Un(x):
    if x == 10:  # this is our base case in the ap problem
        return 5
    else:
        return Un(x + 1) + 1


print(Un(5))
