if __name__ == '__main__':
    s="uihu8"
    cnt_alphanum=0
    cnt_digit=0
    cnt_alpha=0
    cnt_low=0
    cnt_up=0
    for i in range(len(s)):
        if s[i].isalpha():
            cnt_alpha=cnt_alpha+1
        if s[i].isdigit():
            cnt_digit=cnt_digit+1
        if s[i].islower():
            cnt_low=cnt_low+1
        if s[i].isupper():
            cnt_up=cnt_up+1
    if (cnt_alpha>0 or cnt_digit>0):print("True")
    else: print("False")
    if(cnt_alpha>0):print("True")
    else: print("False")
    if(cnt_digit>0):print("True")
    else: print("False")
    if(cnt_low>0):print("True")
    else: print("False")
    if(cnt_up>0):print("True")
    else: print("False")






