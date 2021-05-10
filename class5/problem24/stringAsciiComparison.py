# ascii values are ordered in a way that  lower cases come after capitals
# so, strings have their "sizes" based on sum of ascii of characters
# e.g

st = input("Test Name\n")

if st == "Islam":
    print("Your string is same in size as Islam")
elif st < "Islam":
    print("Your string is less in size than (comes before) Islam")
elif st > "Islam":
    print("Your string greater in size as Islam (comes after)")
