def my_function(v=5):  # two changes here, remove erring == and add colon at end ,   # leave next statement because it has no effect
    v + 10
    return v + 10  # indent the return and make it return the increment
my_function()
print(my_function())  # call the function in the print