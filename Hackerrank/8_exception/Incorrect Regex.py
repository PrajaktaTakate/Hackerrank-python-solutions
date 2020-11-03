"""input
2
.*\+
.*+

op-
True
False
"""

import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)