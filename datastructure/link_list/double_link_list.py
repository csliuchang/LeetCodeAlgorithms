# coding: utf-8
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self._head = node 

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        print("\nthe result of travel：")
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.prev = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next  # while program exited , pre point to the (pos-1)'s position
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:   # list unique one
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


