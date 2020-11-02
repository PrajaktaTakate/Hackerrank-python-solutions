import math
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    array1 = list(map(lambda num: abs(num),array1))
    for digit in array2:
            if math.sqrt(digit) not in array1:
                return False
            array1.remove(math.sqrt(digit))
    return True

def comp_v2(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

a1 = [121, 144, 19, 161, 19, 144, 19, -11]
a2 = [121, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2))
print(comp_v2(a1, a2))
