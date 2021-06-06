# yeah, this failed...i am saddened
# define a function that gets the current bank rate from a website that refreshes or a document that refreshes
def cur_format(money):
    a = ''.join((filter(lambda x: x.isdigit() or x == '.', money)))
    if a == "" or a == ".":
        return 0
    else:
        return a

    # join: it takes an iterable and filter returns "iterable" type


# an iterable is an iteratable variable

rate = 500

# abstract enter currency prompt
# use dict for cyrrency details and list for list of supported currency-naira
sup_cod = ["USD","NGN"]
sup_name = ["Dollar","Naira"]
sup_denom = ["cent","Kobo"]
sup_equiv = [1,500]

supported = list(zip(sup_cod,sup_name,sup_denom,sup_equiv))
print (supported)

# abstract denom prompt
# could ask for cur 1 to conv to cur 2 then abstract rate as unit cur2 equiv in cur1 * cur 1
# if cur1 is naira , choose from cur1 - 2 dict, else cur 2- 1 dict or if/else here

while True:
    print("supported currency codes:")
    print()
    for i in supported:
        print([i][0][0])
    cur1 = input("Enter currency amount to be converted:")

    # currency = input("Enter the amount of currency with: $ for dollar, and # for naira\n")
    # if '$' in currency:
    #     # rate = dict.item.rate
    #     cur_den = input("Enter the amount of cents:")
    #     cur_den = float(cur_format(cur_den))
    #     cur_den /= 100.0
    #     currency = cur_format(currency)
    #     converted = round(rate * (float(currency) +cur_den),2)
    #     print("Your Naira equivalent is:", '#' + str(converted) + 'K')
    #     break
    # if '#' in currency:
    #     cur_den = input("Enter the amount of Kobo:")
    #     currency = cur_format(currency)
    #     cur_den = float(cur_format(cur_den))
    #     cur_den /= 100.0
    #     converted = round(((float(currency) + cur_den)/rate),2)
    #     print("Your Dollar equivalent is:", '$' + str(converted) + 'cents')
    #     break
    # else:
    #     print("Error! adhere to the following specification:")
