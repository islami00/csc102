# using filter X lambda
# define a function that gets the current bank rate from a website that refreshes or a document that refreshes
def cur_format(money):
    return ''.join((filter(lambda x: x.isdigit() or x == '.', money)))
    # join: it takes an iterable and filter returns "iterable" type


# an iterable is an iteratable variable

rate = 500


while True:
    currency = input("Enter the currency with $ for dollar, and # for naira, and '.' before cents or kobo\n")
    if '$' in currency:
        currency = cur_format(currency)
        converted = 500 * currency
        print("Your Naira equivalent is:", '#' + str(converted))
        break
    if '#' in currency:
        currency = cur_format(currency)
        converted = float(currency) / 500
        print("Your Dollar equivalent is:", '$' + str(converted))
        break
    else:
        print("Error! adhere to the following specification:")
        break
