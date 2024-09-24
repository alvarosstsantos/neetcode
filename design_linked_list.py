from typing import Optional


class Node(object):

    def __init__(self, val: int, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, prev=self.head)
        self.head.next = self.tail

    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while (curr.next and i <= index):
            curr = curr.next
            i += 1

        return curr.val

    def addAtHead(self, val: int):
        newNode = Node(val, prev=self.head, next=self.head.next)
        self.head.next.prev = newNode
        self.head.next = newNode

    def addAtTail(self, val: int):
        newNode = Node(val, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def addAtIndex(self, index: int, val: int):
        curr = self.head.next
        i = 0

        while (curr and i < index):
            i += 1
            curr = curr.next

        if (i == index and curr):
            newNode = Node(val, prev=curr.prev, next=curr)
            curr.prev.next = newNode
            curr.prev = newNode

    def deleteAtIndex(self, index: int):
        curr = self.head.next
        i = 0

        while (curr and i < index):
            i += 1
            curr = curr.next

        if (i == index and curr and curr != self.tail):
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


if __name__ == "__main__":

    linked_list = MyLinkedList()
    linked_list.deleteAtIndex(0)
    linked_list.deleteAtIndex(1)
    linked_list.addAtIndex(1, 5)
    assert linked_list.get(0) == -1
    linked_list.addAtIndex(0, 1)
    assert linked_list.get(0) == 1
    linked_list.deleteAtIndex(1)
    linked_list.deleteAtIndex(0)
    assert linked_list.get(0) == -1
    assert linked_list.get(1) == -1
    linked_list.addAtHead(1)
    assert linked_list.get(0) == 1
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)
    assert linked_list.get(1) == 2
    linked_list.deleteAtIndex(1)
    assert linked_list.get(1) == 3
