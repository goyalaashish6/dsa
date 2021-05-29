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


def get_tail(cur):
    tail = cur
    while len(tail.children) != 0:
        tail = tail.children[0]
    return tail


def linearize(cur):
    for c in cur.children:
        linearize(c)

    # run reverse loop from second last child till first child
    for i in range(len(cur.children)-2, -1, -1):
        last = cur.children[i+1]
        s_last = cur.children[i]
        del cur.children[i+1]
        tail = get_tail(s_last)
        tail.children.append(last)


if __name__ == '__main__':
    '''
    input : 
    24
    10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1
    '''
    n = int(input())
    arr = [int(item) for item in input().split()]
    root = construct_tree(arr)
    display_tree(root)
    linearize(root)
    print("after linearize : ")
    display_tree(root)