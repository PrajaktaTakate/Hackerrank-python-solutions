def persistence(n):
    result = str(n)
    count = 0
    while len(str(result)) != 1:
        result = mul(result)
        count += 1
    return count


def mul(num):
    result = 1
    for x in str(num):
        result = int(x) * result
    return result


print(persistence(999))
#persistence = lambda n,c=0: persistence(reduce(lambda x,y:int(x)*int(y),str(n)),c+1) if n >=10 else c


def persistence(n):
    p = 0
    while len(str(n)) > 1:
        n = reduce(lambda x,y: int(x)*int(y), [i for i in str(n)])
        p += 1
    return p