import string

def alphabet_position(text):
    if not text:
        return ""
    str1 = text.split(" ")
    list1 = []
    list2 = []
    op = ""
    for digit in str1:
        for i in digit:
            list1 = list1 + [i]

    for item in list1:
        if item.isalpha():
            list2 = list2 + [str(string.ascii_lowercase.index(item.lower()) + 1)]
            op = " ".join(list2)

    return op

print(alphabet_position("The sunset sets at twelve o' clock."))


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())