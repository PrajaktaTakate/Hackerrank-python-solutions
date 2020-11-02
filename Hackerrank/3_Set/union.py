"""input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
output- 13
"""

if __name__=='__main__':
    n= int(input())
    E= set(map(int, input().split()))
    N=int(input())
    F=set(map(int, input().split()))
    print(len(E.union(F)))
