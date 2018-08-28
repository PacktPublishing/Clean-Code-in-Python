def convert_num(num_str: str):
    """
    >>> convert_num("12345")
    12345

    >>> convert_num("-12345")
    -12345

    >>> convert_num("12345-")
    -12345

    >>> convert_num("-12345-")
    12345
    """
    num, sign = num_str[:-1], num_str[-1]
    if sign == "-":
        return -int(num)
    return int(num_str)
