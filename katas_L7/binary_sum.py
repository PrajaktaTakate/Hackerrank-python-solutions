import math


def add_binary_v1(a, b):
    return bin(a+b)[2:]


def add_binary_v2(a, b):
    return '{0:b}'.format(a + b)

print(add_binary_v1(1, 1))
print(add_binary_v2(1, 1))
