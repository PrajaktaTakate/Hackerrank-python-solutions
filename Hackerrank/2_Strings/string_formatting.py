def print_formatted(number):
    for i in range(1, number + 1):
        width = len(bin(number)) - 2
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

        #print(i,oct(i)[2:],hex(i).upper()[2:],bin(int(i))[2:])
              #bin(i).lstrip('-0b'))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
