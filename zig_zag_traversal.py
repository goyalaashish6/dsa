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


def zig_zag_traversal_one_stack_one_queue(root):
    # assume level starts with 1 (odd)
    # this method uses  queue to print odd level and  stack to print even level

    q = deque()  # queue
    st = deque()  # stack
    q.append(root)
    level = 1
    while q:
        size = len(q)
        for i in range(size):
            front = q.popleft()
            # since even level put it in stack
            if level % 2 == 0:
                st.append(front.data)
            # odd level so print it
            else:
                print(front.data, end=" ")
            for child in front.children:
                q.append(child)

        # print the stack content now
        if level % 2 == 0:
            while st:
                print(st.pop(), end=" ")

        print()
        level += 1


def zig_zag_2_stacks_2(root):
    stack1 = []
    stack2 = []
    stack1.append(root)
    '''
    logic : put root in stack1,
    till stack1 is not empty, print stack top.data; and push stack top's children from left to right in stack2
    till stack2 is not empty, print stack top.data; and push stack top's children from right to left in stack2
    '''
    while stack1 or stack2:
        while stack1:
            top = stack1.pop()
            print(top.data, end=" ")
            for child in top.children:
                stack2.append(child)
        print()

        while stack2:
            top = stack2.pop()
            print(top.data, end=" ")
            for i in range(len(top.children) - 1, -1, -1):  # reverse order
                stack1.append(top.children[i])
        print()


def zig_zag_2_stacks(root):
    main_stack = []
    child_stack = []
    main_stack.append(root)
    level = 1
    while main_stack:
        top = main_stack.pop()
        print(top.data, end=" ")
        if level % 2 == 1:
            for c in top.children:
                child_stack.append(c)
        else:
            for index in range(len(top.children) - 1, -1, -1):
                child_stack.append(top.children[index])

        if not main_stack:
            temp = main_stack
            main_stack = child_stack
            child_stack = temp
            print()
            level += 1


if __name__ == '__main__':
    tree_node_list = [10, 20, 50, None, 60, None, None, 30, 70, 120, None, 80, 110, None, None, 90, 130, None, None, 40,
                      100, None, None, None]  # preorder

    root = construct_tree(tree_node_list)
    display_tree(root)

    print("zig zag traversal using 1 queue and 1 stack :")
    zig_zag_traversal_one_stack_one_queue(root)
    print("zig zag traversal using 2 stacks:")
    zig_zag_2_stacks(root)
    print("zig zag traversal using 2 stacks another method:")
    zig_zag_2_stacks_2(root)