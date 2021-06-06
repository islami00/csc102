rate = 500
currency = input("Enter the currency with $ for dollar, and # for naira\n")
if "$" in currency:
    currency = currency.strip(" $")
    converted = 500 * float(currency)
    converted_to = ["Naira","#"]
elif "#" in currency:
    currency = currency.rstrip(" #")
    converted = float(currency)/500
    converted_to = ["Dollar","$"]
if "$" or "#" in currency:
    print("Your",converted_to[0], "equivalent is:", converted_to[1] + str(converted))
