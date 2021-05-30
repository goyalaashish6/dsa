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


class Pair:
    def __init__(self,node_obj, state):
        self.node_obj = node_obj
        self.state = state


def pre_and_post_iterative(root):
    stack=[]
    preorder=[]
    postorder=[]
    stack.append(Pair(root, 0))
    while stack:
        top = stack[-1]
        if top.state == 0:
            preorder.append(top.node_obj.data)
            top.state += 1
        elif top.state <= len(top.node_obj.children):
            stack.append(Pair(top.node_obj.children[top.state-1], 0))
            top.state += 1
        else:
            popped_node = stack.pop()
            postorder.append(popped_node.node_obj.data)
    print(preorder)
    print(postorder)

if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    '''
       input : 
       24
       10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1
    '''
    root = construct_tree(arr)
    pre_and_post_iterative(root)