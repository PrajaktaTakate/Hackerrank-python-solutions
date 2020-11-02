def find_in_str(string, pos):
    r=string[pos]
    import re
    if re.match(r"\w+", r):
        print("Letter")
    elif re.match(r, r"^\d+"):
        print("Digit")
    else:
        print("not string or letter")

"""
In the above solution re.match() always returns string so first If condition always becomes true
\w+ :
Returns a match where the string contains any word characters 
(characters from a to Z, digits from 0-9, and the underscore _ character)
Use of regular expression for this task is bit overkill 
and we can do as mentioned in `find_in_str_improved` in a simple way
"""
def find_in_str_improved(string, pos):
    r = string[pos]
    if r.isalpha():
        print("Letter")
    elif r.isdigit():
        print("Digit")
    else:
        print("not string or letter")



st="hi 5here 4"
find_in_str_improved(st,4)