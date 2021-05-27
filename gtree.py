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
                    stack[-1].children.append(new_node)   #stack[-1] is stack top/peek
                    stack.append(new_node) #push
            else:
                del stack[-1]  #pop
        return root


def display_tree(cur):
    # add cur data and its children to str1
    str1 = "[" + str(cur.data) + "] ->"
    for d  in cur.children:
        str1 += " "+str(d.data)+","
    str1+= " ."
    print(str1)

    for d in cur.children:
        display_tree(d)


def size_in_gtree(cur):
    size = 1
    for c in cur.children:
        c_size = size_in_gtree(c)
        size += c_size
    return size


def max_in_gtree(cur):
    max = cur.data
    for c in cur.children:
        max_child = max_in_gtree(c)
        if max < max_child:
            max = max_child
    return max


def height_in_gtree(cur):
    height = 0
    for c in cur.children:
        c_height = height_in_gtree(c)
        if height < c_height:
            height = c_height
    return height+1


def level_order_line_wise_two_queues(root):
    main_q = deque()
    child_q = deque()
    main_q.append(root)

    while main_q:
        front = main_q.popleft()  #queue remove
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
            print(front.data,end=" ")
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


def zig_zag_traversal_one_stack_one_queue(root):
    # assume level starts with 1 (odd)
    # this method uses  queue to print odd level and  stack to print even level

    q = deque()    # queue
    st = deque()   # stack
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
            for i in range(len(top.children)-1, -1, -1):  # reverse order
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
            for index in range(len(top.children)-1, -1, -1):
                child_stack.append(top.children[index])

        if not main_stack:
            temp = main_stack
            main_stack = child_stack
            child_stack = temp
            print()
            level += 1

def remove_leaves(cur):
    for i in range(len(cur.children)-1,-1,-1):
        print(cur.children[i].data)


if __name__ == '__main__':
        tree_node_list = [10,20,50,None,60,None,None,30,70,120,None,80,110,None,None,90,130,None,None,40,100,None,None,None]  #preorder
        '''
        n = int(input())
        arr = []
        values = str(input()).split()
        for i in range(n):
            tree_node_list[i] = int(values[i])
        '''
        root = construct_tree(tree_node_list)
        display_tree(root)
        max = max_in_gtree(root)
        print("max in gtree = %s " % max)
        size = size_in_gtree(root)
        print("size in gtree = %s" % size)
        height = height_in_gtree(root)
        print("height in gtree = %s" % height)
        print("level order using 2 queues :")
        level_order_line_wise_two_queues(root)
        print("level order using 1 queue and 1 delimiter :")
        level_order_using_one_queue_and_delimiter(root)
        print("level order using 1 queue")
        level_order_using_one_queue(root)
        print("zig zag traversal using 1 queue and 1 stack :")
        zig_zag_traversal_one_stack_one_queue(root)
        print("zig zag traversal using 2 stacks:")
        zig_zag_2_stacks(root)
        print("zig zag traversal using 2 stacks another method:")
        zig_zag_2_stacks_2(root)