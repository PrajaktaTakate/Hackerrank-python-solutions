"""intro
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
 print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
OP- 200
"""

import collections
_=input()
shoe= list(map(int,input().split()))
col=collections.Counter(shoe)
total=0
for i in range(int(input())):
    size,price=map(int,input().split())
    if col[size]:
        total=total+price
        col[size]-=1
print(total)




