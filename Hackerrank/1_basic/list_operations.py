
def insert_item(lst,e,i):
    lst.insert(int(e),int(i))

def remove_item(lst, e):
    lst.remove(int(e))

def append_item(lst,e):
    lst.append(int(e))

def sort_list(lst):
    lst.sort()

def pop_item(lst):
    lst.pop()

def reverse_list(lst):
    lst.reverse()


if __name__ == '__main__':

    """ N = int(input())
    i=0
    input_cmd=[]
    while i < N:
    input_cmd.append(input())
    i=i+1 """
    N=12
    input_cmd = []
    input_cmd = ["insert 0 5","insert 1 10","insert 0 6","print",
                 "remove 6","append 9","append 1","sort","print","pop","reverse","print"]
    print(input_cmd)
    lst = []
    i = 0
    while i < N:
        if input_cmd[i].split()[0] == "print":
            print(lst)
        elif input_cmd[i].split()[0] == "insert":
            insert_item(lst, input_cmd[i].split()[1],input_cmd[i].split()[2])
        elif input_cmd[i].split()[0] == "append":
            append_item(lst, input_cmd[i].split()[1])
        elif input_cmd[i].split()[0] == "remove":
            remove_item(lst, input_cmd[i].split()[1])
        elif input_cmd[i].split()[0] == "sort":
            sort_list(lst)
        elif input_cmd[i].split()[0] == "pop":
            pop_item(lst)
        elif input_cmd[i].split()[0] == "reverse":
            reverse_list(lst)
        i = i + 1

    print(lst)

