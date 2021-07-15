d = {"c": 1, "A": 2, "n": 0}
t = list(d.items())  # this provides a dict_items object
# which is set-like, so one must convert to list first
print(t, "pre-sort")
t.sort()
# sort is a method without a return value as it modifies the list itself, also: it sorts based on the first value,
# so to sort by values one would have to restructure dictitem
print(t, "post-sort")
