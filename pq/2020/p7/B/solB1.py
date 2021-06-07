def sum_fun(list_of_ids):
    s = 0
    for id in list_of_ids:
        s += str(id)[-1]
    return s
