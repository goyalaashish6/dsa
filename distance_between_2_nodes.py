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


def distance_between_2_nodes(cur, d1, d2):
    l1 = node_to_root_path(cur, d1)
    l2 = node_to_root_path(cur, d2)
    i = len(l1) - 1
    j = len(l2) - 1
    res = -1

    # find LCA , index_i finally point to  distance of d1 from its LCA
    # similarly, index_j will point to distance of d2 from its LCA
    # finally (index_i + index_j) is the answer
    while i >= 0 and j >= 0 and l1[i] == l2[j]:
        res = l1[i]
        index_i = i
        index_j = j
        i -= 1
        j -= 1

    if res == -1:
        return -1

    return index_i + index_j


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    d1 = int(input())
    d2 = int(input())
    root = construct_tree(arr)
    retval = distance_between_2_nodes(root, d1, d2)

    print(retval)