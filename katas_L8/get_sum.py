def get_sum(a, b):
    if a == b:
        return b
    elif b<a:
        sum = 0
        for digit in range(b, a+1):
            sum = sum + digit
        return sum
    else:
        sum = 0
        for digit in range(a, b + 1):
            sum = sum + digit
        return sum


print(get_sum(2,5))
