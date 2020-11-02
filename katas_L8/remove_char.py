def remove_char_v1(s):
    op = ''
    for vchar in range(1, len(s)-1):
        op = op+s[vchar]

    return op

def remove_char_v2(s):
    return s[1:-1]

print(remove_char_v1('abcd'))
print(remove_char_v2('abcd'))