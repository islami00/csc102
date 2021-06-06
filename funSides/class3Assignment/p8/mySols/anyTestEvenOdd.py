# my idea goes as follows:
# first mirror the "divisibleBy" function from set theory
def divisible_by(a, b):
    if a % b == 0:
        return True
    else:
        return False


# store converted array booleans
listOutBool = []


# then input conditions for var, and iterable obj exec.
def test_div_obj(any_input):
    if type(any_input) is list or type(any_input) is tuple or type(any_input) is set:
        print("For each number:")
        for elem in any_input:
            if divisible_by(elem, 2) is True:
                listOutBool.append(True)
            else:
                listOutBool.append(False)
            str_elem = str(elem)
            list_in_bool = []
            for digit in str_elem:
                if divisible_by(int(digit), 2) is True:
                    list_in_bool.append(True)
                else:
                    list_in_bool.append(False)
            even_in_only = all(list_in_bool)
            odd_in_only = not any(list_in_bool)
            even_in_and_odd = not (even_in_only or odd_in_only)
            print(str_elem, "Even only:", even_in_only, "Odd only:", odd_in_only, "even and odd:", even_in_and_odd)
    elif type(any_input) is int:
        print("for each digit:\n")
        str_elem = str(any_input)
        list_in_bool = []
        for digit in str_elem:
            if divisible_by(int(digit), 2) is True:
                list_in_bool.append(True)
            else:
                list_in_bool.append(False)
        even_in_only = all(list_in_bool)
        odd_in_only = not any(list_in_bool)
        even_in_and_odd = not (even_in_only or odd_in_only)
        print(str_elem, "Even only:", even_in_only, "Odd only:", odd_in_only, "even and odd:", even_in_and_odd)


# input here
test_div_obj([1, 1, 123, 1234, 5, 46, 5, 54, 747, 745, 745, 457, 1, 1, 1, 1, 1, 1])
# Test for outer Booleans
evenOnly = all(listOutBool)
oddOnly = not any(listOutBool)
evenAndOdd = not (evenOnly or oddOnly)

print("\nIn array:\n", "EvenOnly:", evenOnly, "oddOnly", oddOnly, "evenAndOdd:", evenAndOdd)
