"""input
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

Print the average marks of the list corrected to 2 decimal places.
78.00

"""

import collections
n=int(input())
col = ",".join(input().split())
student = collections.namedtuple('student',col)
stud=[]
for _ in range(n):
    col1,col2,col3,col4=input().split()
    #print(col1)
    stud.append(student(col1,col2,col3,col4))

avg=0
total=0

print(sum(map(int,map(lambda x: x.MARKS,stud))))
print('{0:.2f}'.format(sum(map(int,[x.MARKS for x in stud]))/n))

