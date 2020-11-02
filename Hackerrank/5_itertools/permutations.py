"""input
HACK 2

 OP-
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

import itertools
word,size=input().split()
print(*[''.join(i) for i in itertools.permutations(sorted(word),int(size))], sep='\n')