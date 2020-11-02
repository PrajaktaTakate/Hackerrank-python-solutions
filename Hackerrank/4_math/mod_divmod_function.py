"""input
177
10
output
17
7
(17, 7)
"""

a,b=int(input()),int(input())
print(a//b,a%b,divmod(a,b),sep='\n')