"""
Sample Input
4
a a c d
2
Sample Output
0.8333
"""

"""from itertools import combinations

_,s,n = input(),input().split(),int(input())
t = list(combinations(s,n))
f = [i for i in t if 'a' in i]
print(len(f)/len(t))"""

import itertools
k,m= map(int,input().split())
h=0
s=0
for i in range(k):
    h=max(map(int,input().split()[1:]))
    s=s+(h*h)
print(s%m)
