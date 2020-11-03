"""input
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

op-
Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""

n,m=map(int,input().split())
r=[]
for i in range(n):
    r.append(list(map(int, input().rstrip().split())))
k=int(input())
r = sorted(r, key=lambda i:i[k])
for i in r:
    print(*i)




