import math
class node:
    def __init__(self, data):
        self.data = data
        self.children = []


def construct_tree(data_list):
    stack = []
    root = None
    for data in data_list:
        if data != -1:
            new_node = node(data)
            if len(stack) == 0:
                root = new_node
                stack.append(root)
            else:
                stack[-1].children.append(new_node)  # stack[-1] is stack top/peek
                stack.append(new_node)  # push
        else:
            del stack[-1]  # pop
    return root


def display_tree(cur):
    # add cur data and its children to str1
    str1 = str(cur.data) + " ->"
    for d in cur.children:
        str1 += " " + str(d.data) + ","
    str1 += " ."
    print(str1)

    for d in cur.children:
        display_tree(d)

floor = -math.inf  # smallest int -infinity
def find_floor(cur, data):
    global floor
    if cur.data < data:  # cur.data < data
        # this area updates floor
        if cur.data > floor:
            floor = cur.data

    for child in cur.children:
        find_floor(child, data)

def kth_largest(root,k):
    global floor
    data = math.inf
    for i in range(k):
        floor = -math.inf
        find_floor(root,data)
        data = floor
    return data

if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    k = int(input())
    '''
       input : 
       24
       10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1
    '''
    root = construct_tree(arr)
    #display_tree(root)
    d = kth_largest (root, k)
    print(d)