def greatest(l_o_digits):
    max_id = None
    for digit in l_o_digits:
        if max_id is None:
            max_id = digit
        if digit > max_id:
            max_id = digit
    return max_id
