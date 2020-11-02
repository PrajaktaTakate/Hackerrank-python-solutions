
"""input
HACK 2

 OP-
A
C
H
K
AC
AH
AK
CH
CK
HK
"""


import itertools
word,size=input().split()
for i in range(1, int(size)+1):
    for j in itertools.combinations(sorted(word), i):
        print(''.join(j))