"""input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5

output= 4
"""

if __name__ == '__main__':
    n=int(input())
    s= set(map(int, input().split()))
    N= int(input())
    cmd=[input() for i in range(N)]
    print(s)
    print(cmd)
    for j in cmd:
        i=j.split()
        if i[0]=='pop' : s.pop()
        if i[0]=='remove':s.remove(int(i[1]))
        if i[0]=='discard':s.discard(int(i[1]))
    print(sum(s))





