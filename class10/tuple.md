#Tuples

tuples only have two methods : index and count.
The tuple is immutable.
It does not have append or remove methods.
We can use modifications to count tuples
We take it from a dictionary, and convert it to a list of tuple,and then use the sorted method.

Things that cannot be done with tuple:
Sort, append, or reversing.
```python
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

```
Tuples are more efficient as they are not structured for modification.
better for temporary variables.

Tuples allow for multiple assignment of variables:
e.g:
```python
(x,y) = (4,5)
```

The dict.items method returns a list of tuples containing the key,value pairs written like that

Tuples also work with comparison operators like strings e.g:

```python
a = (0,1,2) < (5,1,2)

print(a)
```
It evaluates things like an or, i.e., as long as at least one of the pairs of values is true or false,
the only thing it skips is "=" for "<" or ">"

Due to this method of comparison, we can sort tuples using lists.

```python
d = {"c":1, "A":2, "n":0}
t = list(d.items())  # this provides a dict_items object
# which is set-like, so one must convert to list first
print(t,"pre-sort")
t.sort()
# sort is a method without a return value as it modifies the list itself
print(t,"post-sort")
```
```python
d = {"c":1, "A":2, "n":0}
t = set(d.items())  # this provides a dict_items object
# which is set-like, to sort in this case,
# one can easily place it in a set

print(t,"pre-sort")
print(t,"post-sort")
```

**do note: here, we are sorting by the value**

Sort by value:
```python
c = dict()
t = []
for k,v in c.items():
    t.append((v,k))
# this provides us with a
# list of tuple with items of the dictionary reversed
```

We can find the first ten words in a paragraph as in problem46, then in a custom way we can filter to top 10 by using
a slice when printing the sorted values using a for loop i.e `listOfSorted[0:10]`
e.g:

Bonus on slices: `[::1]` actually gives a slice that goes through the entire list in steps of one.
That's right: slice syntax as defined by the `.slice()` method is: `[start:end:step]`
Bonus ++: `str.[::-1]` can be used to print a string in reverse order.
Got both from the w3c schools reference section for py

```python
var = [print(f"{a} {b}")for a,b in sortList[-1:-5:-1]]
# This runs the print function on each value and key in the sorted list which uses custom slicng from the last to the 
# 4th last element in steps of one (indexes from the end of a list use -1...)
# Fstrings are used for varible insertion.
# Also, var will be a list of None as the print function returns None. It's just a context for us to print easily
```