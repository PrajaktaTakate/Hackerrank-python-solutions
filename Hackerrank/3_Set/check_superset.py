"""
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

output
False
"""


if __name__=='__main__':
    A=set(map(int,input().split()))
    for _ in range(int(input())):
        if not A.issuperset(set(map(int,input().split()))):
            print("False")
            exit()
    print("True")


"""a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))
"""

