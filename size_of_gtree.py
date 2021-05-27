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


def size_in_gtree(cur):
    size = 0
    for c in cur.children:
        c_size = size_in_gtree(c)
        size += c_size
    return size+1


if __name__ == '__main__':
    '''
    n = int(input())
    arr = [int(item) for item in input().split()]
    '''
    arr = [10, 20, 50, None, 60, None, None, 30, 70, 120, None, 80, 110, None, None, 90, 130, None, None, 40,
                      100, None, None, None]  # preorder

    root = construct_tree(arr)
    display_tree(root)
    size = size_in_gtree(root)
    print("size in gtree = %s" % size)