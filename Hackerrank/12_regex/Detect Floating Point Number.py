"""
input
4
4.0O0
-1.00
+4.54
SomeRandomStuff

op-
False
True
True
False
"""
import re
for _ in range(int(input())):
	print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
