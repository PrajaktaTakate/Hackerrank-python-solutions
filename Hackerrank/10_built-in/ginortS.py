"""
input
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Sorting1234
op-
ginortS1324
"""

#4 solutions
s=input()

print(*sorted(s, key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(s, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(s, key=order.index), sep='')

import string
print(*sorted(s, key=(string.ascii_letters + '1357902468').index), sep='')