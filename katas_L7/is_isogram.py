def is_isogram_v1(string):
    str = string.lower()
    if str != '':
        for i in str:
            if str.count(i) >= 2:
                return False

    return True


def is_isogram_v2(string):
    print(set(string.lower()))
    return len(string) == len(set(string.lower()))


print(is_isogram_v1("isoogram"))
print(is_isogram_v2("isoogram"))
