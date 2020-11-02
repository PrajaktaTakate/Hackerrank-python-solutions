"""input
7
UK
China
USA
France
New Zealand
UK
France
"""

if __name__ == '__main__':
    n=int(input())
    stamp=set(input() for i in range(n))
    print(len(stamp))
