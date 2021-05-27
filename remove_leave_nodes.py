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


def removeLeaves(cur):
    siz = len(cur.children)-1
    for i in range(siz, -1, -1):
        if not cur.children[i].children:
            del cur.children[i]
        else:
            removeLeaves(cur.children[i])


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]

    root = construct_tree(arr)
    #display_tree(root)
    removeLeaves(root)
    display_tree(root)
