# function typecasting to show errors

def interest(r: int, t: int, p: float):
    SI = float(p) * int(r) * int(t) / 100
    return SI


print(interest(1, 2, 1.3))
