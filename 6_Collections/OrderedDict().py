"""
input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

OP-
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""

from collections import OrderedDict

n = int(input())
item = OrderedDict()
for _ in range(n):
    data = input().split()
    key, val = ' '.join(data[:-1]), int(data[-1])
    item[key] = item.get(key, 0)

    # if key not in item.keys():
    #     item[key] = 0
    item[key] += val

print(*item.items(), sep='\n')
for (key, val) in item.items():
    print(key, val)
