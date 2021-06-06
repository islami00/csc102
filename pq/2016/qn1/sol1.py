# collect money
cents = int(input("Enter cents:\n"))

# dollar, quarters, dimes, nickels and pennies(in that order)
# $1=100 cents
# 1 quarter= 25 cents
# 1 dime= 10 cents
# 1 nickel = 5 cents
# 1 penny= 1 cent

dollars = cents // 100
quarters = cents // 25
dimes = cents // 10
nickels = cents // 5
pennies = cents // 1

print("Number of dollars:",dollars)
print("Number of quarters:",quarters)
print("Number of dimes:",dimes)
print("Number of nickels:",nickels)
print("Number of pennies:",pennies)
