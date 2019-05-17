# coding:utf-8
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node

    def is_empty(self):
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self._head
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        print("\nthe result of travel：")
        while cur.next != self._head:
            print(cur.elem, end=" ")
            cur = cur.next
        # exit the cycle and print the last node
        print("\nlast elem not be traveled", cur.elem)

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # exit the cycle and cur point to the last node
            node.next = self._head
            self._head = node
            cur.next = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head    # node.next = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next  # while program exited , pre point to the (pos-1)'s position
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.elem == item:
                if cur == self._head:
                    rear = self._head   # for the situation as head node ,find last node
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self._head:
                self._head = None
            else:
                pre.next = self._head  # pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False


if __name__ == "__main__":
    l1 = SingleCycleLinkList()
    print(l1.is_empty())
    print(l1.length())

    l1.append(1)
    print(l1.is_empty())
    print(l1.length())
    l1.append(2)
    l1.add(8)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l1.append(6)
    l1.insert(-1, 9)
    l1.travel()
    l1.insert(2, 100)
    l1.travel()
    l1.insert(10, 200)
    l1.travel()
    print(l1.search(100))
    l1.remove(9)
    l1.travel()
    l1.remove(200)
    l1.travel()
