"""input
 ABC is a right triangle, 90 at B.
Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find MBC (angle , as shown in the figure) in degrees.

10
10
output
45
"""

import math
AB = int(input())
BC = int(input())
print(str(int(round(math.degrees(math.atan2(AB,BC)))))+'°')
