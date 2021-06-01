#dictionaries
This isn't like a list which is a linear collection without labels,
rather, it gives labels to the values  
It is powerful as it allows for database like operations
DIfferent names:  
Associatiive arrays: php/perl  
properties or HAshMap : java  
They are no longer sorted like sets, rather they are ordered.

ways of making dicts
```python
nppl= dict()
cor = {}
```

Also, dictionaries are **MUTABLE**
i.e
```python
nppl = {
    "MyNigga" : 1
}
nppl["MyNigga"] = nppl["MyNigga"] + 1
```

anything that can be done with list indexes can be done with dictionary keys  
Thus, a dictionary structure is:  
```python
road = {
    "key" : "value"
}
```

A dictionary can be applied in statistics for counting frequencies.  
i.e counting multiple lists.

We can't reference a key that isnt in a dictionry.
Use in to test keys i.e

```python
ccc = {}
ccc["csev"] = "dalema"
print("csev" in ccc)
```
That code will return true cuz csev is a key of ccc
Thus, "in" checks keys of dict

lists are displayed as tuples (formatted as: (,)  
lists only use keys, so the list() function returns a list of the keys in a dictionaries  
.item method returns a list with the key value pairs as 2-tuples.  
 we can use dictionaries as 2d arrays too i.e for a,b in dict.items  