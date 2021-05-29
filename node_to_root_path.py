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


def node_to_root_path(cur, data):
    if cur.data == data:
        lis = []
        lis.append(data)
        return lis

    for child in cur.children:
        ret_list = node_to_root_path(child, data)
        if ret_list:
            ret_list.append(cur.data)
            return ret_list
    return []


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    '''
       input : 
       24
       10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1
    '''
    root = construct_tree(arr)
    display_tree(root)
    ret_list = node_to_root_path(root, 90)
    print(ret_list)