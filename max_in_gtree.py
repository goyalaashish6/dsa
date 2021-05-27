from collections import deque


class node:
    def __init__(self, data):
        self.data = data
        self.children = []


def construct_tree(data_list):
    stack = []
    root = None
    for data in data_list:
        if data is not None:
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


def max_in_gtree(cur):
    max = cur.data
    for c in cur.children:
        max_child = max_in_gtree(c)
        if max < max_child:
            max = max_child
    return max


if __name__ == '__main__':
    tree_node_list = [10, 20, 50, None, 60, None, None, 30, 70, 120, None, 80, 110, None, None, 90, 130, None, None, 40,
                      100, None, None, None]  # preorder

    root = construct_tree(tree_node_list)
    display_tree(root)
    max = max_in_gtree(root)
    print("max in gtree = %s " % max)
