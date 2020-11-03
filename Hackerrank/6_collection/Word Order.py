"""
input
4
bcdef
abcdefg
bcde
bcdef

op-
3
2 1 1
"""

import collections
n=int(input())
words= collections.OrderedDict()
for i in range(n):
    key=str(input())
    if key not in words.keys():
        words[key]=0
    words[key]+=1
print(len(words))
print(*words.values())
