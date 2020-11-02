def average(array):
    n = len(set(array))
    print(n)
    av = sum(set(array))/n
    print(av)

if __name__ == '__main__':

    average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174])