if __name__ == '__main__':
    records = []
    """for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])"""
    records=[['a', 20.0], ['b', 30.0],['c',10.0],['d',50.0],['e', 20.0]]
    print(records)
    second_lowest = sorted(set(x[1] for x in records))[1]
    new_list =[]
    for i in records:
        if i[1]==second_lowest:
            new_list.append(i)
    new_list.sort()
    for x in new_list:
        print(str(x[0]))
