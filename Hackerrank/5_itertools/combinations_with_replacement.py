
"""input
HACK 2

 OP-
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""


import itertools
word,size=input().split()
print(*[''.join(i) for i in itertools.combinations_with_replacement(sorted(word),int(size))], sep='\n')
