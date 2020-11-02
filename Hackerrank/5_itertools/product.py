"""input
Output the space separated tuples of the cartesian product.
 1 2
 3 4
 OP-
(1, 3) (1, 4) (2, 3) (2, 4)
"""
import itertools
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*itertools.product(a,b))
