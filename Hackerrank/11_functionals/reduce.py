"""
input
Print only one line containing the numerator and denominator of the product
of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.
3
1 2
3 4
10 6

op-
5 8
"""
import functools
from fractions import Fraction
k=[]
for i in range(int(input())):
    n,d= map(int,input().split())
    k.append(n/d)
print(Fraction(functools.reduce(lambda n,d: n*d,k)))
