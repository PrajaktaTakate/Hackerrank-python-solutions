#!/bin/python3
import math
import os
import random
import re
import sys

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    else:
        if 2<= n <=5:
            print("Not Weird")
        elif 6 <= n <=20:
            print("Weird")
        elif n>20:
            print("Not Weird")