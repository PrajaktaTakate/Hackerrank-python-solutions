import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    s=s.split(" ")
    cap=[i.capitalize() for i in s ]
    print(" ".join(cap))


if __name__ == '__main__':
    solve('hello   world  lol')
    solve('132 456 Wq  m e')



