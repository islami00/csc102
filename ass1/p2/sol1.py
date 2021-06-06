def my_function(v=5):  # two changes here, remove erring == and add colon at end, next line left for no effect
    v + 10
    return v + 10  # indent the return and make it return the increment
my_function()
print(my_function(50))  # call the function in the print