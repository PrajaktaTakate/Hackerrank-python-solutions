"""input
Print True if p(x)=k. Otherwise, print False.
1 4
x**3 + x**2 + x + 1

True
"""

x,k=map(int,input().split())
p=input().replace('x', str(x))
print(eval(p)==k)
