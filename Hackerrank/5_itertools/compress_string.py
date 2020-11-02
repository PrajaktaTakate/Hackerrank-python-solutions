"""
Sample Input
1222311
Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
"""
import itertools
s=input()
print(*[(len(list(g)),int(k)) for k,g in itertools.groupby(s)])