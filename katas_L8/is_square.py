import math


def is_square_v1(n):
    if n < 0:
        return False
    elif math.sqrt(n).is_integer():
        return True
    else:
        return False


def is_square_v2(n):
    return n >= 0 and math.sqrt(n).is_integer()


print(is_square_v1(5))
print(is_square_v2(5))
