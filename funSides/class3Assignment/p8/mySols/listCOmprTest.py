def even_or_odd(a):
    filt = [True if c % 2 == 0 else False for c in a if isinstance(c, int)]
    if len(filt) == len(a):
        if all(filt):
            return "Even"
        elif any(filt):
            return "Even and Odd"
        else:
            return "Odd"
    else:
        return "Invalid Input"


# This can also be swapped as the last and first are pretty much two sides of the same completely general coin
# the wrapper if statement is used to handle cases of invalid input format
print(even_or_odd([3, 3]))
