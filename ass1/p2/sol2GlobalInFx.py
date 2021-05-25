def my_function(x=5):  # three changes here, remove erring == and add colon at end, and change name of parameter to fit print call
    global v # make the called v in print global
    v = x + 10; return v  # assign to v the parameter increment and return it.
my_function()
print(v)
