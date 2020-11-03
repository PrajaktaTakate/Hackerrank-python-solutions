"""
input
5
op-
A list on a single line containing the cubes of N the first  fibonacci numbers.
[0, 1, 1, 8, 27]
"""
# n=int(input())
# lst=[0,1]
# for i in range(2,n):
#     lst.append(lst[i-2]+lst[i-1])
# print(list(map(lambda i: i*i*i,lst)))


cube = lambda x: x*x*x # complete the lambda function

def fibonacci(n):
    lst=[0,1]
    for i in range(2,n):
        lst.append(lst[i-2]+lst[i-1])
    return lst[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))