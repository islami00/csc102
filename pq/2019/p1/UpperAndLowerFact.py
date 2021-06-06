def falling_fact(base):
    if base == 1 or base == 0:  # here, we define a minimum
        return 1
    else:
        return base * falling_fact(base - 1)


def rising_fact(base, upper_limit):
    if upper_limit == 0:
        return 1
    else:
        return base * rising_fact(base + 1, upper_limit - 1)


def rising_fact_bottom(base, upper_limit, zeroth=0):
    if zeroth == upper_limit:
        return 1
    else:
        return base * rising_fact_bottom(base + 1, upper_limit, zeroth + 1)


print(falling_fact(5))  # 5!
print(rising_fact(5, 5) * -1)  # coefficient of the fifth derivative of x**-5
print(rising_fact_bottom(5, 5) * -1)  # coefficient of the fifth derivative of x**-5
