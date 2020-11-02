"""input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
output - 8
"""

#((sum(myset)*k)-(sum(arr)))//(k-1)

if __name__=='__main__':
    k=int(input())
    room=input().split()
    room.sort()
    print((set(room[0::2]) ^ set(room[1::2])).pop())

