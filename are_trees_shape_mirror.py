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


def are_trees_mirror_in_shape(cur1, cur2):
    if len(cur1.children) != len(cur2.children):
        return False
    # now length of cur1.children and length of cur2.children are equal
    i = 0
    j = len(cur2.children) - 1

    while i < len(cur1.children):
        if not are_trees_mirror_in_shape(cur1.children[i], cur2.children[j]):
            return False
        i += 1
        j -= 1

    return True


if __name__ == '__main__':
    n = int(input())
    arr1 = [int(item) for item in input().split()]
    root1 = construct_tree(arr1)

    m = int(input())
    arr2 = [int(item) for item in input().split()]
    root2 = construct_tree(arr2)
    # display_tree(root)
    if are_trees_mirror_in_shape(root1, root2):
        print("true")
    else:
        print("false")


