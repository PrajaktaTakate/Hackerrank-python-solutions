def minion_game(string):
    Stuart=[]
    Kevin=[]
    kevsc=0
    stusc=0
    vowels='AEIOU'
    l=len(string)
    for i in range(l):
        if string[i] in vowels:
            kevsc += (l - i)
            print(kevsc)
        else:
            stusc += (l - i)
            #print(stusc)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")
"""" for i in range(l):
        if string[i].lower() not in ['a','e','i','o','u']:
            for j in range(l-i):
                Stuart.append(string[-j:l])
        else:
            for j in range(l-i):
                Kevin.append(string[-j:l])
    if len(Stuart)>len(Kevin):
        print("Stuart",len(Stuart))
    elif len(Stuart)<len(Kevin):
        print("Kevin",len(Kevin))
    else:
        print("Draw")
"""



if __name__ == '__main__':
    minion_game('BANANA')