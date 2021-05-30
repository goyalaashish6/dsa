#5star important

from collections import deque


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
    str1 = "[" + str(cur.data) + "] ->"
    for d in cur.children:
        str1 += " " + str(d.data) + ","
    str1 += " ."
    print(str1)

    for d in cur.children:
        display_tree(d)


def height(cur):
    h = -1
    for c in cur.children:
        c_height = height(c)
        if h < c_height:
            h = c_height
    return h + 1


def diameter(cur):
    max_height = second_max_height  = -1
    for child in cur.children:
        height_of_child = height(child)
        if height_of_child >= max_height:
            second_max_height = max_height
            max_height = height_of_child
        elif height_of_child > second_max_height:
            second_max_height = height_of_child

    dia_from_child = 0
    for child in cur.children:
        dia_from_child = max(dia_from_child, diameter(child))

    return max(dia_from_child, max_height+second_max_height+2)


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    '''
       input : 
       24
       10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1
    '''
    root = construct_tree(arr)
    dia = diameter(root)
    print(dia)