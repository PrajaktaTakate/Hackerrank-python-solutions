"""
input
5
12 9 61 5 14
op-
True
"""

_,no= input(),list(map(int,input().split()))
print(all(i > 0 for i in no) and any(str(i)==str(i)[::-1] for i in no))




