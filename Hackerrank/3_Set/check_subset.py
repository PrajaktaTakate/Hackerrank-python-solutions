"""input
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
output -
True
False
False
"""


if __name__=='__main__':
    n=int(input())
    output = []
    for i in range(n):
        (_,A,_,B)=(int(input()),set(map(int,input().split())),int(input()),set(map(int,input().split())))
        if A.issubset(B):output.append("True")
        else: output.append("False")
    print(*output,sep='\n')
