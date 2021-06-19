

PI = 3.14

primelist = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]


def doubleit(arg):
    if not isinstance(arg, (int, float)):
        raise TypeError('arg must be int or float')
    darg = arg * 2
    return darg

