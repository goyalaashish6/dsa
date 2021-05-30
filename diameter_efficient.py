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


overall_diameter = 0


def find_diameter_using_modified_height(cur):
    global overall_diameter
    max_height = -1
    second_max_height = -1
    for child in cur.children:
        height_of_child = find_diameter_using_modified_height(child)
        if height_of_child >= max_height:
            second_max_height = max_height
            max_height = height_of_child
        elif height_of_child > second_max_height:
            second_max_height = height_of_child

    overall_diameter = max(overall_diameter, max_height+second_max_height+2)  # update diameter
    return max_height + 1   # return height of this level


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    '''
       input : 
       24
       10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1
    '''
    root = construct_tree(arr)
    height = find_diameter_using_modified_height(root)
    print(overall_diameter)