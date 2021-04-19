def big(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(big(1, 2, 4))
print(max(1, 2, 4))


