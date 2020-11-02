def order(sentence):
    if sentence == "":
        op = ""
        return op
    str1 = sentence.split(" ")
    list1 = []
    for digit in str1:
        str1 = sorted(digit)[:1]
        list1 = list1 + [[int(str1[0]), digit]]
        list2 = sorted(list1, key=lambda x: x[0])
    list3 = [item[1] for item in list2]
    print(list3)
    op = " ".join(list3)
    return op


print(order("is2 Thi1s T4est 3a"))
