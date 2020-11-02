"""input
1+2j
output
 2.23606797749979
 1.1071487177940904
"""

import cmath
print(*cmath.polar(complex(input())), sep='\n')