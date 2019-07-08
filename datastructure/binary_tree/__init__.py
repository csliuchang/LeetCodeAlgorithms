# coding:utf-8


class Node(object):
    """


    """
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        queue = [self.root]

        cur_node = queue.pop(0)
        if cur_node.lchild is None:
            cur_node.lchild is node
            return
        else:



