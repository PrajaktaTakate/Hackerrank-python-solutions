if __name__ == '__main__':
    inp=input().split()
    N=int(inp[0])
    M=int(inp[1])
    print(N , M)
    for i in range(1,N,2):
        print((('.|.')*(i)).center(M,'-'))
    print(('WELCOME').center(M,'-'))
    for i in reversed(range(0,N-1,2)):
        print((('.|.') * (i + 1)).center(M, '-'))
