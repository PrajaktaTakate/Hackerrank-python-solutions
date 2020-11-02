"""input
4
2 4 5 9
4
2 4 11 12

output
5
9
11
12
"""

m=int(input())
M=set(map(int,input().split()))
n=int(input())
N=set(map(int,input().split()))
diff = sorted(M.symmetric_difference(N))
print(*diff,sep='\n')


"""
a,b = [set(raw_input().split()) for i in range(4)][1::2]
print ('\n'.join(sorted(a^b, key=int)))

a,b = [set(input().split()) for i in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')
"""