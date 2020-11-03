"""input
6
append 1
append 2
append 3
appendleft 4
pop
popleft

OP-
1 2
"""
import collections
d=collections.deque()
# for i in range(int(input())):
#     cmd = input().split()
#     if cmd[0] == 'append': d.append(int(cmd[1]))
#     if cmd[0] == 'appendleft': d.appendleft(int(cmd[1]))
#     if cmd[0] == 'pop': d.pop()
#     if cmd[0] == 'popleft': d.popleft()
# print(*d)

for i in range(int(input())):
    cmd,*arg= input().split()
    getattr(d,cmd)(*arg)
print(*d)