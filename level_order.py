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


def level_order_line_wise_two_queues(root):
    main_q = deque()
    child_q = deque()
    main_q.append(root)

    while main_q:
        front = main_q.popleft()  # queue remove
        print(front.data, end=" ")
        for child in front.children:
            child_q.append(child)
        if not len(main_q):
            print()
            temp = main_q
            main_q = child_q
            child_q = temp


def level_order_using_one_queue_and_delimiter(root):
    q = deque()
    q.append(root)
    q.append(None)
    while q:
        front = q.popleft()
        if front is not None:
            print(front.data, end=" ")
            for child in front.children:
                q.append(child)
        else:
            print()
            if q:
                q.append(None)


def level_order_using_one_queue(root):
    q = deque()
    q.append(root)
    while q:
        size = len(q)
        for i in range(size):
            front = q.popleft()
            print(front.data, end=" ")
            for child in front.children:
                q.append(child)
        print()


if __name__ == '__main__':
    tree_node_list = [10, 20, 50, None, 60, None, None, 30, 70, 120, None, 80, 110, None, None, 90, 130, None, None, 40,
                      100, None, None, None]  # preorder

    root = construct_tree(tree_node_list)
    display_tree(root)
    print("level order using 2 queues :")
    level_order_line_wise_two_queues(root)
    print("level order using 1 queue and 1 delimiter :")
    level_order_using_one_queue_and_delimiter(root)
    print("level order using 1 queue")
    level_order_using_one_queue(root)
