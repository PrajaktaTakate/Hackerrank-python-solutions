"""input
ou are given three integers: Print two lines.
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).
3
4
5
OP-
81
1
"""

a,b,m=int(input()),int(input()),int(input())
print(pow(a,b),pow(a,b,m),sep='\n')