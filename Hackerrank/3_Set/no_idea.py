if __name__ == '__main__':
    (n,m) = input().split()
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(n)
    print(m)
    print(arr)
    print(A)
    print(B)
    happy=0
    for i in arr:
        if i in A: happy=happy+1
        if i in B: happy=happy-1
    print(happy)

