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


state = 0
pred = -1
succ = -1


def pred_success(cur, data):
    global state, pred, succ
    if state == 0:
        if cur.data == data:
            state = 1
        else:
            pred = cur.data
    elif state == 1:
        succ = cur.data
        state = 2

    for child in cur.children:
        if state != 2:
            pred_success(child, data)


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    data = int(input())
    root = construct_tree(arr)
    pred_success(root, data)
    print("Predecessor = " + str(pred))
    print("Successor = " + str(succ))

