"""
A decorator that returns 'YES' if decorated function returns non-false value.

"""


# region YES/NO Decorator

def ynDec(function):
    def inner1(*args, **kwargs):
        res = function(*args, **kwargs)
        if res:
            return 'YES'
        return 'NO'

    return inner1

# endregion
