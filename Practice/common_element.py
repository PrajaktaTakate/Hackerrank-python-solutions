

def num_of_comman_elements(l1,l2):
    print(l1)
    print(l2)
    cnt=0
    inter=0
    for i in l1:
       if i in l2:
                cnt=cnt+1
       inter = inter +1
    print(inter)
    return cnt

def num_of_comman_elements2(l1,l2):
    print(l1)
    print(l2)
    return len(set(l1).intersection(l2))



l2 = [2, 3, 4, 7, 10, 21, 25, 27, 30,37]
l1 = [2, 5, 10, 22, 27, 30, 37]

print(num_of_comman_elements(l1, l2))