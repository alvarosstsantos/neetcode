from typing import List


class Node:

    def __init__(self, value: int, next: 'Node'):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = None

        for i in range(0, index + 1):
            curr = curr.next if curr else self.head

            if not curr:
                return -1

        return curr.value

    def insertHead(self, value: int) -> None:
        node = Node(value, self.head)

        self.head = node

        if not self.tail:
            self.tail = node

    def insertTail(self, value: int) -> None:
        node = Node(value, None)

        if self.tail:
            self.tail.next = node

        self.tail = node

        if not self.head:
            self.head = node

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            return False

        curr = None

        for _ in range(0, index):
            curr = curr.next if curr else self.head

            if not curr:
                return False

        if curr.next:
            if not curr.next.next:
                self.tail = curr

            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head

        while (curr):
            arr.append(curr.value)
            curr = curr.next

        return arr
