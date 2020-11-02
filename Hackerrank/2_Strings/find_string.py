def count_substring(string, sub_string):
    cnt=0
    for i in range(len(string)):
        if string[i:len(sub_string)+i]==sub_string:
            cnt= cnt+1
    return cnt

if __name__ == '__main__':
    print(count_substring('prajaktatakate','ta'))
