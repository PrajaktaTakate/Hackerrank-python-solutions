"""
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

output
78.00
"""

import collections
n, Score = int(input()) , collections.namedtuple('Score',input().split())
scores = [Score(*input().split()).MARKS for i in range(n)]
print("%.2f"% (sum(map(int,scores))/n))