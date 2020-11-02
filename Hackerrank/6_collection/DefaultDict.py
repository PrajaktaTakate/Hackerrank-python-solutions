"""input
5 2
a
a
b
a
b
a
b

op-
1 2 4
3 5
"""
import collections
m,n= map(int,input().split())
A=collections.defaultdict(list)
B=[]
for i in range(m):
    A[input()].append(i+1)

for i in range(n):
    B.append(input())
for i in B:
    if i in A:
        print(*A[i])
    else:
        print(-1)

print(A)
print(B)
